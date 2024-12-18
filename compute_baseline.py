import json
import os
import statistics

from tqdm import tqdm

from execution.execution import Execution


def main(
    model_output: str,
    type: str,
    score_dir: str = "results/scores/",
):
    data = []
    with open(model_output, "r") as file:
        for line in file:
            data.append(json.loads(line))

    tasks = []
    for _, output in enumerate(data):
        task = {
            "modified_program": output["modification"],
            "refactored_program": output["original"],
            "entry_point": output["entry_point"],
            "tests": output["tests"],
        }
        tasks.append(task)

    codeforces_accurate = 0
    humaneval_accurate = 0
    codeforces_cpu = []
    humaneval_cpu = []
    codeforces_memory = []
    humaneval_memory = []
    codeforces_size = []
    humaneval_size = []
    codeforces_complexity = []
    humaneval_complexity = []
    outputs = []

    for task in tqdm(tasks):
        framework = Execution(
            {
                "original_program": task["modified_program"],
                "refactored_program": task["refactored_program"],
                "entrypoint_name": task["entry_point"],
                "test_code": task["tests"],
            },
            timeout=5.0,
        )

        result = framework.run()
        outputs.append(result)

        if result["correctness"]:
            if type == "CodeForces":
                codeforces_accurate += 1
                codeforces_cpu.append(result["performance"]["instruction_change"])
                codeforces_memory.append(result["performance"]["memory_change"])
                codeforces_size.append(result["size"]["change"])
                codeforces_complexity.append(result["complexity"]["change"])
            else:
                humaneval_accurate += 1
                humaneval_cpu.append(result["performance"]["instruction_change"])
                humaneval_memory.append(result["performance"]["memory_change"])
                humaneval_size.append(result["size"]["change"])
                humaneval_complexity.append(result["complexity"]["change"])

    with open(
        score_dir + os.path.splitext(os.path.basename(model_output))[0] + ".json", "w"
    ) as f_out:
        if type == "CodeForces":
            content = {
                "codeforces": {
                    "codeforces_accurate": codeforces_accurate / 100,
                    "codeforces_cpu": statistics.mean(codeforces_cpu),
                    "codeforces_memory": statistics.mean(codeforces_memory),
                    "codeforces_size": statistics.mean(codeforces_size),
                    "codeforces_complexity": statistics.mean(codeforces_complexity),
                }
            }
        else:
            content = {
                "humaneval": {
                    "humaneval_accurate": humaneval_accurate / 100,
                    "humaneval_cpu": statistics.mean(humaneval_cpu),
                    "humaneval_memory": statistics.mean(humaneval_memory),
                    "humaneval_size": statistics.mean(humaneval_size),
                    "humaneval_complexity": statistics.mean(humaneval_complexity),
                }
            }
        print(content)
        content["individual"] = outputs
        f_out.write(json.dumps(content))


if __name__ == "__main__":
    from fire import Fire

    Fire(main)
