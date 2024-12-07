import json
import os


def read_jsonl_file(file_path: str, num_entries: int, modification: str):
    entries = []
    with open(file_path, "r") as file:
        for i, line in enumerate(file):
            if i >= num_entries:
                break
            result = json.loads(line)
            result["type"] = modification
            entries.append(result)
    return entries


def main(
    output_path: str,
    num_entries: int = 33,
):
    # Hacky for now but it is okay, just class project
    jsonl_files = [
        ("OBFUSCATE", "dataset/HumanEval/HumanEvalPlus-Refactor-Obfuscate.jsonl"),
        ("DEAD_CODE", "dataset/HumanEval/HumanEvalPlus-Refactor-DeadCode.jsonl"),
        ("INEFFICIENCY", "dataset/HumanEval/HumanEvalPlus-Refactor-Inefficiency.jsonl"),
    ]
    all_entries = []

    for index, (modification, jsonl_file) in enumerate(jsonl_files):
        if index == 0:
            num_entries += 1

        entries = read_jsonl_file(jsonl_file, num_entries, modification)
        all_entries.extend(entries)

        if index == 0:
            num_entries -= 1

    with open(output_path, "w") as file:
        for entry in all_entries:
            file.write(json.dumps(entry) + "\n")


if __name__ == "__main__":
    from fire import Fire

    Fire(main)
