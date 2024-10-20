import enum
import json
import os

import openai
from tqdm import tqdm

from request.openai import make_auto_request
from utility.parser import remove_comments

CAPTURE_HEAD = "<code_start>"
CAPTURE_TAIL = "<code_end>"

# TODO: Refine prompt and prompt types

INSTRUCTION_DEAD_CODE = f"""\
Given the following code snippet, insert dead code into the code snippet. \
The dead code should decrease readability of the \
snippet but should not should change the execution of the code. Do not generate any comments. \
The variable names should also be blended with the input program. Try your best to make \
it appear that there is no dead code in the snippet. Make as many unobvious changes as you \
can.
"""

INSTRUCTION_OBFUSCATE = f"""\
Assume you are an malicious engineer who is trying to obfuscate code, you are given a sample code snippet \
and your job is to make the code as unreadable and inefficient as possible. However the code should still \
maintain the same purpose, execution flow and outputs. Try to make the inefficiencies as hidden as possible. Do not include any comments that \
make it obvious you have added the inefficiencies.
"""

INSTRUCTION_INEFFICIENCY = f"""\
Given the following code snippet, increase the execution complexity of the code. \
The inefficiencies can change the execution flow and should increase the total number of \
instructions and make the code less efficient \
However, the new code should not should change the output or the purpose of the code. Assume that \
the input code is valid and does not contain any bugs. Try to make the inefficiencies as \
not obvious and hidden as possible. Do not include any comments that \
make it obvious you have added the inefficiencies.
"""


def make_prompt(code: str, instruction: str):
    return f"""\
{instruction}

```
{code}
```

{instruction}

Please follow format to complete the skeleton below:

{CAPTURE_HEAD}
Modified code snippet here
{CAPTURE_TAIL}
"""


class ModifyType(enum.Enum):
    DEAD_CODE = INSTRUCTION_DEAD_CODE
    INEFFICIENCY = INSTRUCTION_INEFFICIENCY
    OBFUSCATE = INSTRUCTION_OBFUSCATE


# Modify input data to create refactor dataset
def main(
    dataset_path: str,
    modify_type: ModifyType,
    output_path: str,
    debug: bool = False,
):
    data = []
    with open(dataset_path, "r") as file:
        for line in file:
            data.append(json.loads(line))

    try:
        modify_type = ModifyType[modify_type]
    except KeyError:
        print("Invalid modification type")
        exit(1)

    tasks = []
    for problem in data:
        original_solution = remove_comments(
            problem["prompt"] + problem["canonical_solution"]
        )
        task = {
            "prompt": make_prompt(modify_type.value, original_solution),
            "task_id": problem["task_id"],
            "entry_point": problem["entry_point"],
            "test": problem["entry_point"],
            "original_solution": original_solution,
        }
        tasks.append(task)

    with open(output_path, "+a") as f_out:
        for task in tqdm(tasks):
            client = openai.Client()
            output = make_auto_request(
                client,
                task["prompt"],
                model="gpt-4o",
                max_tokens=2048,
                temperature=0.2,
                n=1,
            )
            annotation = output.choices[0].message.content
            result = {
                "name": task["task_id"],
                "prompt": task["prompt"],
                "original": original_solution,
                "raw_modification": annotation,
                "modification": remove_comments(
                    annotation.split(CAPTURE_HEAD)[-1].split(CAPTURE_TAIL)[0]
                ),
            }
            json.dump(result, f_out)
            f_out.write("\n")
            f_out.flush()

            # TODO: Check against test cases, only accept modification if test cases pass

            if debug:
                print("Modified Output", "-" * 80)
                print(result["modification"])
                print("-" * 80)
                print("Enter to continue... or b to break:")
                if input() == "b":
                    break


if __name__ == "__main__":
    from fire import Fire

    Fire(main)
