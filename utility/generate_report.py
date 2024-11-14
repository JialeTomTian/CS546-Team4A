import os
import subprocess
from pathlib import Path
import pandas as pd
from datetime import datetime
import sys


def execute_py_files(folder_path):
    folder = Path(folder_path)
    py_files = list(folder.glob('*.py'))

    results = []
    for py_file in py_files:
        try:
            result = subprocess.run([sys.executable, str(py_file)],
                                    capture_output=True,
                                    text=True,
                                    timeout=30)

            if result.returncode == 0 and result.stdout:

                try:
                    time_us, mem_kb = map(float, result.stdout.strip().split())
                    results.append({
                        'filename': py_file.name,
                        'execution_time_microsecond': time_us,
                        'memory_usage_kb': mem_kb,
                        'status': 'success',
                        'error': None
                    })
                except ValueError:
                    results.append({
                        'filename': py_file.name,
                        'execution_time_microsecond': None,
                        'memory_usage_kb': None,
                        'status': 'output_format_error',
                        'error': 'Invalid output format'
                    })
            else:
                results.append({
                    'filename': py_file.name,
                    'execution_time_microsecond': None,
                    'memory_usage_kb': None,
                    'status': 'failed',
                    'error': result.stderr
                })

        except subprocess.TimeoutExpired:
            results.append({
                'filename': py_file.name,
                'execution_time_microsecond': None,
                'memory_usage_kb': None,
                'status': 'timeout',
                'error': 'Execution timed out'
            })
        except Exception as e:
            results.append({
                'filename': py_file.name,
                'execution_time_microsecond': None,
                'memory_usage_kb': None,
                'status': 'error',
                'error': str(e)
            })

    return results


def generate_report(results, output_folder=None):

    df = pd.DataFrame(results)

    successful_runs = df[df['status'] == 'success']

    stats = {
        'Total files': len(df),
        'Successful runs': len(successful_runs),
        'Failed runs': len(df) - len(successful_runs),
        'Average time (μs)': successful_runs['execution_time_microsecond'].mean(),
        'Max time (μs)': successful_runs['execution_time_microsecond'].max(),
        'Min time (μs)': successful_runs['execution_time_microsecond'].min(),
        'Average memory (kb)': successful_runs['memory_usage_kb'].mean(),
        'Max memory (kb)': successful_runs['memory_usage_kb'].max(),
        'Min memory (kb)': successful_runs['memory_usage_kb'].min()
    }

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    if output_folder:
        output_folder = Path(output_folder)
        output_folder.mkdir(exist_ok=True)

        df.to_csv(output_folder / f'performance_results_{timestamp}.csv', index=False)

        with open(output_folder / f'performance_summary_{timestamp}.txt', 'w') as f:
            f.write("Performance Test Summary\n")
            f.write("=" * 50 + "\n")
            for key, value in stats.items():
                if isinstance(value, float):
                    f.write(f"{key}: {value:.2f}\n")
                else:
                    f.write(f"{key}: {value}\n")

    return df, stats


if __name__ == '__main__':

    folder_path = './canonical_solution'
    output_folder = './reports'

    results = execute_py_files(folder_path)

    df, stats = generate_report(results, output_folder)


    print("\nPerformance Test Summary")
    print("=" * 50)
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"{key}: {value:.2f}")
        else:
            print(f"{key}: {value}")

    print("\nDetailed Results:")
    print("=" * 50)
    for result in results:
        print(f"\nFile: {result['filename']}")
        print(f"Status: {result['status']}")
        if result['status'] == 'success':
            print(f"Execution Time: {result['execution_time_microsecond']:.4f} μs")
            print(f"Memory Usage: {result['memory_usage_kb']:.4f} kb")
        if result['error']:
            print(f"Error: {result['error']}")