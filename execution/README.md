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
To locally execute a specific entry, replace the `benchmark_entry` in the `main()` function with the desired entry and run the execution.py script:
```bash
python execution.py
```

### Run the Dataset

To run the dataset, use the following command:
```bash
python run.py --dataset=<path_to_your_dataset> [--logs=<path_to_log>] [--results=<path_to_save_result>]
```
* `--dataset`: Path to the JSON dataset (Required).
* `--logs`: Path to store the logs (Optional). Default is `execution/logs/`.
* `--results`: Path to save the results (Optional). Default is `execution/result.json`.

#### Example Usage
To run with the default paths for logs and results:
```bash
python run.py --dataset=sample.json
```
To specify a custom log and result path:
```bash
python run.py --dataset=sample.json --logs=/path/to/logs --results=/path/to/result.json
```

