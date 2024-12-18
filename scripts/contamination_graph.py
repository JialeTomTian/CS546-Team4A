models = [
    "results/scores/gpt-4o-COMBINED.json",
    "results/scores/Qwen-Qwen2.5-Coder-14B-Instruct-COMBINED.json",
]


import json

import matplotlib.pyplot as plt
import numpy as np

width = 0.35
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))


model_data = {}

graphs = [ax1, ax2]

for model in models:
    with open(model, "r") as file:
        data = json.load(file)
        model_data[model] = {}
        model_data[model]["humaneval"] = data["humaneval"]
        model_data[model]["codeforces"] = data["codeforces"]

field_processing = ["accurate", "cpu", "size"]

datasets = ["humaneval", "codeforces"]

categories = ["Accuracy", "CPU", "Size Reduction"]

titles = [
    "Refactoring Improvements for GPT-4o",
    "Refactoring Improvements for Qwen Coder 2.5",
]
x = np.arange(len(categories))

for index, model in enumerate(models):
    human_eval = []
    codeforces = []
    for field in field_processing:
        human_eval.append(model_data[model]["humaneval"]["humaneval_" + field])

    for field in field_processing:
        codeforces.append(model_data[model]["codeforces"]["codeforces_" + field])

    bar1 = graphs[index].bar(x - width / 2, human_eval, width, label="HumanEval")
    bar2 = graphs[index].bar(x + width / 2, codeforces, width, label="Codeforces")

    graphs[index].set_xlabel("Evaluated Metrics", fontsize=18)
    graphs[index].set_ylabel("% Improvement", fontsize=18)
    graphs[index].set_title(titles[index], fontsize=18)
    graphs[index].set_xticks(x)
    graphs[index].set_xticklabels(categories, fontsize=18)
    graphs[index].legend(fontsize=18)
    graphs[index].grid(True)
# Display plot
plt.tight_layout(h_pad=3)
plt.savefig("contamination_graph.png", dpi=600)
