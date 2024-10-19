import enum
import json
import os

import openai
from tqdm import tqdm

CAPTURE_HEAD = "<code_start>"
CAPTURE_TAIL = "<code_end>"


class ModifyType(enum.Enum):
    DEAD_CODE = "dead_code"
    INEFFICIENCY = "inefficiency"
    COMBINATION = "combination"


# Modify input data to create refactor dataset
def main(
    dataset_path: str,
    modify_type: ModifyType,
):
    pass


if __name__ == "__main__":
    from fire import Fire

    Fire(main)
