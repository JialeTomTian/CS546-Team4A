# CS546-Team4A
Evaluating Code Refactoring Capabilities of LLMs (CS546 Final Project)

## Running the Benchmarks:
You can directly run the benchmarks and save the outputs direct into `results/model_outputs`.
Currently, you can use the vllm and hf backends.

### vllm backend
```shell
python refactor_eval.py --model=deepseek-ai/deepseek-coder-6.7b-instruct --backend=vllm
```

### hf backend
```shell
python refactor_eval.py --model=deepseek-ai/deepseek-coder-6.7b-instruct --backend=hf
```

The results will be automatically parsed and stored within jsonl files with the apprioriate naming.

## About Benchmarks
The benchmarks for this project are stored in `dataset/Benchmark`
- `dataset/Benchmark/CodeForces-Modify-Merged.jsonl`: A set of 100
codeforces solutions found in the wild modified by GPT-4o to enable more refactoring
- `dataset/Benchmark/HumanEvalPlus-Modify-Merged.jsonl`: A set of 100
HumanEval canonical solutions modified by GPT-4o to enable more refactoring

For each dataset, three modification strategies are performed: obfuscation,
dead code and inefficiencies. With a 34, 33, 33 split across the 100 problems.

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
