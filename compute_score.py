import json
import os
import statistics

from tqdm import tqdm

from execution.execution import Execution


def main(
    model_output: str,
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
            "refactored_program": output["output"],
            "entry_point": output["entry_point"],
            "tests": output["tests"],
            "benchmark": output["benchmark"],
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
            if task["benchmark"] == "CodeForces":
                codeforces_accurate += 1
                codeforces_cpu.append(result["performance"]["instruction_change"])
                codeforces_memory.append(result["performance"]["memory_change"])
                codeforces_size.append(result["size"]["change"])
            else:
                humaneval_accurate += 1
                humaneval_cpu.append(result["performance"]["instruction_change"])
                humaneval_memory.append(result["performance"]["memory_change"])
                humaneval_size.append(result["size"]["change"])

    with open(
        score_dir + os.path.splitext(os.path.basename(model_output))[0] + ".json", "w"
    ) as f_out:
        content = {
            "combined": {
                "combined_accurate": (codeforces_accurate + humaneval_accurate) / 200,
                "combined_cpu": statistics.mean(codeforces_cpu + humaneval_cpu),
                "combined_memory": statistics.mean(
                    codeforces_memory + humaneval_memory
                ),
                "combined_size": statistics.mean(codeforces_size + humaneval_size),
            },
            "codeforces": {
                "codeforces_accurate": codeforces_accurate / 100,
                "codeforces_cpu": statistics.mean(codeforces_cpu),
                "codeforces_memory": statistics.mean(codeforces_memory),
                "codeforces_size": statistics.mean(codeforces_size),
            },
            "humaneval": {
                "humaneval_accurate": humaneval_accurate / 100,
                "humaneval_cpu": statistics.mean(humaneval_cpu),
                "humaneval_memory": statistics.mean(humaneval_memory),
                "humaneval_size": statistics.mean(humaneval_size),
            },
        }
        print(content)
        content["individual"] = outputs
        f_out.write(json.dumps(content))


if __name__ == "__main__":
    from fire import Fire

    Fire(main)
