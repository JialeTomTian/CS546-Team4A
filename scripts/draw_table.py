import json
import os


def read_json_files(directory):
    model_mapping = {}
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            model_name = filename[:-14]
            with open(filepath, "r") as file:
                data = json.load(file)
                model_mapping[model_name] = data["combined"]
                model_mapping[model_name]["ranks"] = []

    field_processing = [
        "combined_accurate",
        "combined_cpu",
        "combined_memory",
        "combined_size",
        "combined_complexity",
    ]

    for field in field_processing:
        sort_list = []
        for model in model_mapping:
            sort_list.append((model, model_mapping[model][field]))
        sort_list.sort(key=lambda x: x[1], reverse=True)

        for index, (name, _) in enumerate(sort_list):
            model_mapping[name][field] = (model_mapping[name][field], index + 1)
            model_mapping[name]["ranks"].append(index + 1)

    for model in model_mapping:
        model_mapping[model]["ranks"] = sum(model_mapping[model]["ranks"]) / len(
            model_mapping[model]["ranks"]
        )

    sort_ranks = []
    for model in model_mapping:
        sort_ranks.append((model_mapping[model]["ranks"], model, model_mapping[model]))

    sort_ranks.sort(key=lambda x: x[0])

    for index, (_, name, model) in enumerate(sort_ranks):
        print(
            f"{index + 1} & {name} & {(model['combined_accurate'][0]* 100):.2f} & {(model['combined_cpu'][0] * 100):.2f} & {(model['combined_memory'][0] * 100):.2f} & {(model['combined_size'][0] * 100):.2f} & {(model['combined_complexity'][0] * 100):.2f} & {model['ranks']:.2f} \\\\"
        )


if __name__ == "__main__":
    directory = "results/scores"
    data = read_json_files(directory)
