## Program Execution Framework
### Format of the entry in the dataset
Each entry in the dataset should be in the following format:
```json
{
    "original_program": "some_code",
    "refactored_program": "some_code",
    "entrypoint_name": "some_code",
    "test_code": "some_code"
}
```

### Locally Execute an Entry
There are two ways to execute the single entry:

**1. Diretly modify the `execution.py`**:

To locally execute a specific entry, replace the variable `benchmark_entry` in the `main()` function with the desired entry and run the execution.py script:
```bash
python execution.py
```
It will print the result directly in the terminal.

**2. Run the `run.py` with args**:
```bash
python run.py --type=entry --entry=[json string]
```
For example:
```bash
python run.py --type=entry --entry="{\"original_program\": \"def subtract(a, b):\\n    result = a\\n    result -= b\\n    return result\\n\", \"refactored_program\": \"def subtract(a, b):\\n    return a - b\\n\", \"entrypoint_name\": \"subtract\", \"test_code\": \"def check(func):\\n    assert func(5, 3) == 2\\n    assert func(-1, 1) == -2\\n    assert func(0, 0) == 0\\n\"}"
```
It will print the result directly in the terminal.

### Run the Dataset

To run the dataset, use the following command:
```bash
python run.py --type=dataset --dataset=<path_to_your_dataset> [--log=<path_to_log>] [--result=<path_to_save_result>]
```
* `--type`: Specify the type: 'dataset' to run on a JSON dataset or 'entry' to run a single entry."
* `--dataset`: Path to the JSON dataset (Required).
* `--log`: Path to store the logs (Optional). Default is `execution/logs/`.
* `--result`: Path to save the results (Optional). Default is `execution/result.json`.

#### Example Usage
To run with the default paths for logs and results:
```bash
python run.py --type=dataset --dataset=sample.json
```
To specify a custom log and result path:
```bash
python run.py --type=dataset --dataset=sample.json --log=/path/to/logs --result=/path/to/result.json
```
