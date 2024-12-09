import contextlib
import importlib.util
import multiprocessing
import os
import signal
import tempfile
import time
import tracemalloc
from typing import Any, Callable, Dict, List, Tuple

from cirron import Collector  # type: ignore
from radon.metrics import h_visit  # type: ignore
from transformers import AutoTokenizer  # type: ignore

# Not the best idea but let's just do all our analysis here for now
# If this becomes a real project, we can consider refactoring

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
        size = self._compare_size(self.original_program, self.refactored_program)
        complexity = self._compare_complexity(original_results, refactored_results)

        return {
            "correctness": correctness,
            "performance": performance,
            "original_results": original_results,
            "refactored_results": refactored_results,
            "size": size,
            "complexity": complexity,
        }

    def _compare_size(
        self, original_program: str, refactored_program: str
    ) -> Dict[str, Any]:
        tokenizer = AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-Instruct-hf")

        original_size = len(tokenizer.tokenize(original_program))
        new_size = len(tokenizer.tokenize(refactored_program))

        return {
            "original_size": original_size,
            "new_size": new_size,
            "change": (original_size - new_size) / original_size,
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
        performance = {"instructions": 0, "memory": 0}

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
                    with Collector() as collector:
                        exec(check_program, exec_globals)
                    results["status"] = "passed"
                    results["instructions"] = int(collector.counters.instruction_count)
                    performance["instructions"] = int(
                        collector.counters.instruction_count
                    )
            except TimeoutException:
                results["status"] = "timed out"
            except Exception as e:
                results["status"] = f"failed: {e}"

            performance["memory"] = tracemalloc.get_traced_memory()[1]
        finally:
            tracemalloc.stop()
            os.remove(temp_file.name)

        return results, performance

    def _compare_complexity(
        self, original_results: Dict[str, Any], refactored_results: Dict[str, Any]
    ) -> Dict[str, str]:
        try:
            halsteed_original = h_visit(self.original_program).total.volume
            halsteed_refactored = h_visit(self.refactored_program).total.volume

            return {
                "original": halsteed_original,
                "refactored": halsteed_refactored,
                "change": (halsteed_original - halsteed_refactored) / halsteed_original,
            }
        except Exception as e:
            return {
                "original": 0,
                "refactored": 0,
                "change": 0,
            }

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
            "original_instructions": original_perf["instructions"],
            "refactored_instructions": refactored_perf["instructions"],
            "instruction_change": (
                original_perf["instructions"] - refactored_perf["instructions"]
            )
            / original_perf["instructions"],
            "original_memory": original_perf["memory"],
            "refactored_memory": refactored_perf["memory"],
            "memory_change": (original_perf["memory"] - refactored_perf["memory"])
            / original_perf["memory"],
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
    if False:
        result += 1
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
    print("Complexity:", results["complexity"])
    print("Original Program Results:", results["original_results"])
    print("Refactored Program Results:", results["refactored_results"])

"""
Expected to output:

Correctness: True
Performance: {'runtime': 'faster', 'memory': 'more efficient'}
Original Program Results: {'status': 'passed'}
Refactored Program Results: {'status': 'passed'}

"""
