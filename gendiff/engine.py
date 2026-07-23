import json
from pathlib import Path

import yaml

PATH_1 = "assets/file1.json"
PATH_2 = "assets/file2.json"


def files_to_dict(path_1, path_2):
    format = Path(path_1).suffix

    if format == ".json":
        data_1 = json.load(open(path_1))
        data_2 = json.load(open(path_2))
    if format in (".yaml", ".yml"):
        with open(path_1, "r", encoding="utf-8") as f:
            data_1 = yaml.safe_load(f)
        with open(path_2, "r", encoding="utf-8") as f:
            data_2 = yaml.safe_load(f)

    return data_1, data_2


def generate_diff(path_1=PATH_1, path_2=PATH_2, format="stylish"):
    data_1, data_2 = files_to_dict(path_1, path_2)

    all_data = sorted(set(data_1.keys()) | set(data_2.keys()))

    result = []
    for k in all_data:
        if k in data_1.keys() and k in data_2.keys() and data_1[k] == data_2[k]:
            result.append(f"    {k}: {json.dumps(data_1[k])}")
        else:
            if k in data_1:
                result.append(f"  - {k}: {json.dumps(data_1[k])}")
            if k in data_2:
                result.append(f"  + {k}: {json.dumps(data_2[k])}")

    result = "{\n" + "\n".join(result) + "\n}"
    return result
