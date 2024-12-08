import contextlib
import importlib.util
import multiprocessing
import os
import signal
import tempfile
import time
import tracemalloc
from typing import Any, Callable, Dict, List, Tuple


# Define the input/output interface
class Execution:
    """
    input format:
        {
        "original_program": some_code,
        "refactored_program": some_code,
        "entrypoint_name": some_code,
        "test_code": some_code
        }
    """

    def __init__(self, benchmark_entry: Dict[str, Any], timeout: float = 5.0):
        self.original_program = benchmark_entry["original_program"]
        self.refactored_program = benchmark_entry["refactored_program"]
        self.entrypoint_name = benchmark_entry["entrypoint_name"]
        self.test_code = benchmark_entry["test_code"]
        self.timeout = timeout

    def run(self) -> Dict[str, Any]:
        original_results, original_perf = self._execute_code(
            self.original_program, "original"
        )
        refactored_results, refactored_perf = self._execute_code(
            self.refactored_program, "refactored"
        )

        correctness = self._check_correctness(original_results, refactored_results)
        performance = self._compare_performance(original_perf, refactored_perf)

        return {
            "correctness": correctness,
            "performance": performance,
            "original_results": original_results,
            "refactored_results": refactored_results,
        }

    # hacky method to run single program without comparison
    def single_run(self) -> Dict[str, Any]:
        original_results, original_perf = self._execute_code(
            self.original_program, "original"
        )

        return {"correctness": original_results["status"], "perf": original_perf}

    def _execute_code(
        self, code: str, label: str
    ) -> Tuple[Dict[str, Any], Dict[str, float]]:
        results = {}
        performance = {"runtime": 0, "memory": 0}

        with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp_file:
            temp_file.write(code.encode())
            module_name = os.path.splitext(os.path.basename(temp_file.name))[0]

        try:
            spec = importlib.util.spec_from_file_location(module_name, temp_file.name)
            module = importlib.util.module_from_spec(spec)

            try:
                with time_limit(self.timeout):
                    spec.loader.exec_module(module)
            except IndentationError as e:
                # Indentation error
                results["status"] = f"failed: IndentationError: {str(e)}"
                return results, performance
            except Exception as e:
                results["status"] = f"failed: {e}"
                return results, performance
            except TimeoutException:
                results["status"] = "timed out"
                return results, performance

            start_time = time.time()
            tracemalloc.start()

            try:
                with time_limit(self.timeout):
                    exec_globals = {}
                    check_program = (
                        code
                        + "\n"
                        + self.test_code
                        + f"\ncheck({self.entrypoint_name})"
                    )
                    exec(check_program, exec_globals)
                    results["status"] = "passed"
            except TimeoutException:
                results["status"] = "timed out"
            except Exception as e:
                results["status"] = f"failed: {e}"

            end_time = time.time()
            performance["runtime"] = end_time - start_time
            performance["memory"] = tracemalloc.get_traced_memory()[1]
        finally:
            tracemalloc.stop()
            os.remove(temp_file.name)

        return results, performance

    def _check_correctness(
        self, original_results: Dict[str, Any], refactored_results: Dict[str, Any]
    ) -> bool:
        return (
            original_results.get("status")
            == refactored_results.get("status")
            == "passed"
        )

    def _compare_performance(
        self, original_perf: Dict[str, float], refactored_perf: Dict[str, float]
    ) -> Dict[str, str]:
        return {
            "runtime": "faster"
            if refactored_perf["runtime"] < original_perf["runtime"]
            else "slower",
            "memory": "more efficient"
            if refactored_perf["memory"] < original_perf["memory"]
            else "less efficient",
        }


@contextlib.contextmanager
def time_limit(seconds: float):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")

    signal.signal(signal.SIGALRM, signal_handler)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)


class TimeoutException(Exception):
    pass


def single_execution(
    input_program: str, test_cases: str, entry_point: str
) -> Dict[str, Any]:
    """
    execution of singluar program and return statistics
    """

    framework = Execution(
        {
            "original_program": input_program,
            "refactored_program": "",
            "entrypoint_name": entry_point,
            "test_code": test_cases,
        }
    )

    return framework.single_run()


if __name__ == "__main__":
    # example
    # need to ensure the correctness of indentation
    benchmark_entry = {
        "original_program": """
def add(a, b):
    result = a
    result += b
    return result
""",
        "refactored_program": """
def add(a, b):
    return a + b
""",
        "entrypoint_name": "add",
        "test_code": """
def check(func):
    assert func(2, 3) == 5
    assert func(-1, 1) == 0
    assert func(0, 0) == 0
""",
    }

    framework = Execution(benchmark_entry, timeout=2.0)
    results = framework.run()

    print("Correctness:", results["correctness"])
    print("Performance:", results["performance"])
    print("Original Program Results:", results["original_results"])
    print("Refactored Program Results:", results["refactored_results"])

"""
Expected to output:

Correctness: True
Performance: {'runtime': 'faster', 'memory': 'more efficient'}
Original Program Results: {'status': 'passed'}
Refactored Program Results: {'status': 'passed'}

"""
