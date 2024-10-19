# CS546-Team4A
Evaluating Code Refactoring Capabilities of LLMs (CS546 Final Project)


## Repo Structure

- `curation`: Scripts to perform dataset curation and creation
  - `modify.py`: Prompt GPT to perform modifacation on original
- `dataset`: HumanEval and OpenSource Datasets
  - `HumanEvalPlusOrig.jsonl`: Original HumanEval Problems

## Development Beginner Notice

### After clone

```shell
pip install pre-commit
pre-commit install
pip install -r requirements.txt
```

### Import errors?

```shell
# Go to the root path of RepoQA
export PYTHONPATH=$PYTHONPATH:$(pwd)
```
