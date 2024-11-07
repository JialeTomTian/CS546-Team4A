import logging
import os
import argparse
import json
from execution import Execution
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)
from datetime import datetime

# Setup logging function
def setup_logging(log_path: str):
    if not os.path.exists(log_path):
        os.makedirs(log_path, exist_ok=True)

    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_file = os.path.join(log_path, f'execution_{current_time}.log')

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='w'
    )

setup_logging('logs')

def run_dataset(dataset_path: str, log_path: str, result_file_path: str):
    with open(dataset_path, 'r') as f:
        dataset = json.load(f)

    # Variables to track statistics
    total_entries = len(dataset)
    successful_entries = 0
    correct_refactor = 0
    timeout_entries = 0
    results_list = []

    progress_bar = Progress(
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        BarColumn(),
        MofNCompleteColumn(),
        TextColumn("•"),
        TimeElapsedColumn(),
        TextColumn("•"),
        TimeRemainingColumn(),
    )

    with progress_bar as p:
        task = p.add_task("Running Dataset", total=total_entries)

        for benchmark_entry in dataset:
            try:
                framework = Execution(benchmark_entry, timeout=2.0)
                results = framework.run()
                logging.info(f"Processed entry: {benchmark_entry['entrypoint_name']} - Correctness: {results['correctness']}")

                results_list.append({
                    'entrypoint_name': benchmark_entry['entrypoint_name'],
                    'original_results': results['original_results'],
                    'refactored_results': results['refactored_results'],
                    'correctness': results['correctness'],
                })
                if results["original_results"]["status"] == "passed" and results["refactored_results"]["status"] == "passed":
                    successful_entries += 1
                if results["correctness"]:
                    correct_refactor += 1
                if results["original_results"]["status"] == "timed out" or results["refactored_results"]["status"] == "timed out":
                    timeout_entries += 1
            except Exception as e:
                logging.error(f"Error processing entry {benchmark_entry['entrypoint_name']}: {e}")

            p.update(task, advance=1)

    # Write to result file in JSON format
    summary = {
        'total_entries': total_entries,
        'successful_entries': successful_entries,
        'correct_refactor': correct_refactor,
        'timeout_entries': timeout_entries
    }

    try:
        final_results = {
            'results': results_list,
            'summary': summary
        }
        with open(result_file_path, 'w') as result_file:
            json.dump(final_results, result_file, indent=4)
        logging.info(f"Results and summary successfully written to {result_file_path}")
    except Exception as e:
        logging.error(f"Error writing results to file: {e}")



def main():
    parser = argparse.ArgumentParser(description="Run code execution framework on dataset.")
    parser.add_argument("--dataset", help="Path to the JSON dataset", default="sample.json")
    parser.add_argument("--log", help="Path to store the logs", default="logs", nargs="?")
    parser.add_argument("--result", help="Path to store the results", default="result.json", nargs="?")
    
    args = parser.parse_args()

    run_dataset(args.dataset, args.log, args.result)

if __name__ == '__main__':
    main()
