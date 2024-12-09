import os
import subprocess


# recompute the scores, really bad script
def main():
    folder_path = "results/model_outputs"
    script_path = "/home/tom/fastd/fuzz-jvm/bin/python"
    compute_script = "compute_score.py"

    # Get all files in the folder
    files = os.listdir(folder_path)

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            # Run the command for each file
            command = ["sudo", script_path, compute_script, file_path]
            subprocess.run(command)


if __name__ == "__main__":
    main()
