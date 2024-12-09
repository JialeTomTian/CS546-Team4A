import json
import os
import re
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

Please follow format to complete the skeleton below:

{CAPTURE_HEAD}
Refactored code snippet here
{CAPTURE_TAIL}
"""


def main(
    model: str,
    backend: str,
    benchmark: Benchmark = Benchmark.COMBINED,
    result_dir: str = "results/model_outputs",
    base_url: str = None,
    trust_remote_code: bool = False,
    max_new_tokens: int = 512,
    debug: bool = False,
    tensor_parallel_size: int = 2,
    max_model_len: int = 1024,
    compute_results: bool = True,
    score_dir: str = "results/scores",
):
    if backend == "openai":
        from request.openai import OpenAIProvider

        engine = OpenAIProvider(model, base_url=base_url)
    elif backend == "vllm":
        from request.vllm import VllmProvider

        engine = VllmProvider(
            model,
            trust_remote_code=trust_remote_code,
            tensor_parallel_size=tensor_parallel_size,
            max_model_len=max_model_len,
        )
    elif backend == "hf":
        from request.hf import HfProvider

        engine = HfProvider(
            model,
            trust_remote_code=trust_remote_code,
        )

    os.makedirs(result_dir, exist_ok=True)
    model_output_path = os.path.join(
        result_dir,
        f"{model.replace('/', '-')}-{str(benchmark.name)}.jsonl",
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
                    parsed_block = remove_comments(
                        output.split(CAPTURE_HEAD)[-1].split(CAPTURE_TAIL)[0]
                    )

                    search_pattern = r"^```(?:\w+)?\s*\n(.*?)(?=^```)```"
                    code_blocks = re.findall(
                        search_pattern, parsed_block, re.DOTALL | re.MULTILINE
                    )
                    if code_blocks:
                        parsed_output = code_blocks[0]
                    else:
                        parsed_output = parsed_block
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

    if compute_results:
        from compute_score import main as compute_score

        compute_score(model_output_path, score_dir)


if __name__ == "__main__":
    from fire import Fire

    Fire(main)
