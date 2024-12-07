import os
import re

from datasets import load_dataset

from execution.execution import single_execution


def generate_code_wrapper(original_program: str, task_name: str) -> str:
    indent = "\t"  # Create the indentation string
    indented_code = "\n".join(
        f"{indent}{line}" for line in original_program.splitlines()
    )
    return f"""
def {task_name}():
    {indented_code}
    """


def generate_test_code(test_cases: str):
    return f"""
def check(function):
    import io
    from unittest.mock import patch
    test_cases = {test_cases}
    for i, case in enumerate(test_cases):
        input_val = case['input']
        output = case['output']
        with patch('builtins.input', side_effect=input_val.split(\"\\n\")):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:  # Capture print
                function()
                # Assert the print output
                assert mock_stdout.getvalue().strip() == output.strip()
    """


def main(dataset_path: str, debug: bool = False):
    # Load the dataset
    dataset = load_dataset("evanellis/codeforces_with_only_correct_completions")

    tests_mapping = {}
    # Iterate through the dataset
    for example in dataset["train"]:
        # Access the fields in each example
        contestId = str(example["contestId"])
        index = example["index"]
        if example["verdict"] != "OK":
            continue
        tests_mapping[(contestId, index)] = {
            "test_cases": example["test_cases"],
            "task_name": "_".join(
                re.sub(r"[^a-zA-Z0-9]", "", example["name"]).split(" ")
            ),
        }

    solutions_paths = "dataset/CodeForces/CodeForces-Solutions/Programs"

    tasks = []

    # recursively open through python files within solutions paths
    for root, dirs, files in os.walk(solutions_paths):
        for file in files:
            if file.endswith(".py"):
                # open the file
                with open(os.path.join(root, file)) as input_file:
                    # read the file
                    original_program = input_file.read()
                    original_program = re.sub(
                        r"\bexit\(\)", "return()", original_program
                    )
                    original_program = re.sub(
                        r"\bquit\(\)", "return()", original_program
                    )
                    # get the contestId and index from the file name
                    match = re.match(r"(\d+)([a-zA-Z]+)", file)
                    if match:
                        contestId = match.group(1)
                        index = match.group(2).upper()
                    else:
                        continue

                    if (contestId, index) in tests_mapping:
                        test_cases = tests_mapping[(contestId, index)]["test_cases"]
                        task_name = tests_mapping[(contestId, index)]["task_name"]
                        tasks.append(
                            (
                                original_program,
                                test_cases,
                                str(contestId) + index,
                                task_name,
                            )
                        )
                    else:
                        continue

    print(len(tasks))
    for original_program, test_cases, task_id, task_name in tasks:
        # # generate the test code
        code_wrapper = generate_code_wrapper(original_program, task_name)
        test_code = generate_test_code(test_cases)
        execution_results = single_execution(code_wrapper, test_code, task_name)
        if debug:
            print("Modified Output", "-" * 80)
            print(code_wrapper + test_code)
            print(execution_results)
            print("Enter to continue... or b to break:")
            if input() == "b":
                break


if __name__ == "__main__":
    from fire import Fire

    Fire(main)
