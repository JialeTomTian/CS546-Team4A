import json
import os
from enum import Enum
from typing import Any, Dict

from utility.parser import remove_comments
from utility.utility import progress


class Benchmark(Enum):
    HUMAN_EVAL = [("dataset/Benchmark/HumanEvalPlus-Modify-Merged.jsonl", "HumanEval")]
    CODE_FORCES = [("dataset/Benchmark/CodeForces-Modify-Merged.jsonl", "CodeForces")]
    COMBINED = [
        ("dataset/Benchmark/HumanEvalPlus-Modify-Merged.jsonl", "HumanEval"),
        ("dataset/Benchmark/CodeForces-Modify-Merged.jsonl", "CodeForces"),
    ]


CAPTURE_HEAD = "<code_start>"
CAPTURE_TAIL = "<code_end>"

INSTRUCTION = (
    "Given the below code snippet, please refactor the code to improve its",
    " readability, maintainability, and performance. You can assume that the program",
    " is correct. Do not modify the function signature or the function name."
    " The output and behavior of the function should remain the same.",
)


def construct_prompt(code: str) -> str:
    return f"""{INSTRUCTION}

```
{code}
```

Please follow format to complete the skeleton below (do not wrap in format string):

{CAPTURE_HEAD}
Modified code snippet here
{CAPTURE_TAIL}
"""


def main(
    model: str,
    backend: str,
    benchmark: Benchmark = Benchmark.COMBINED,
    result_dir: str = "results/model_outputs",
    base_url: str = None,
    trust_remote_code: bool = False,
    max_new_tokens: int = 1024,
    debug: bool = False,
):
    if backend == "openai":
        from request.openai import OpenAIProvider

        engine = OpenAIProvider(model, base_url=base_url)
    elif backend == "vllm":
        from request.vllm import VllmProvider

        engine = VllmProvider(
            model,
            trust_remote_code=trust_remote_code,
        )

    os.makedirs(result_dir, exist_ok=True)
    model_output_path = os.path.join(
        result_dir,
        f"{model.replace('/', '-')}-{str(benchmark)}.jsonl",
    )

    tasks = []
    for file_path, benchmark_type in benchmark.value:
        with open(file_path, "r") as file:
            for line in file:
                task = json.loads(line)
                task["benchmark"] = benchmark_type
                tasks.append(task)

    with open(model_output_path, "a") as f_out:
        with progress(f"Running {model}") as pbar:
            for task in pbar.track(tasks):
                prompt = construct_prompt(task["modification"])
                output = engine.generate_reply(
                    prompt,
                    n=1,
                    max_tokens=max_new_tokens,
                )[0]
                try:
                    parsed_output = remove_comments(
                        output.split(CAPTURE_HEAD)[-1].split(CAPTURE_TAIL)[0]
                    )
                except:
                    parsed_output = ""

                if debug:
                    print("Model Output", "-" * 80)
                    print(parsed_output)
                    print("Enter to continue... or b to break:")
                    if input() == "b":
                        break

                result = {
                    **task,
                    "output": parsed_output,
                    "benchmark": task["benchmark"],
                }
                f_out.write(json.dumps(result) + "\n")
                f_out.flush()


if __name__ == "__main__":
    from fire import Fire

    Fire(main)
