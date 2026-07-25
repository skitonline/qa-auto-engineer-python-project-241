import json
from pathlib import Path

import yaml


def parse_files(path_1, path_2):
    format = Path(path_1).suffix

    if format == ".json":
        data_1 = json.load(open(path_1))
        data_2 = json.load(open(path_2))

    if format in (".yaml", ".yml"):
        with open(path_1, "r", encoding="utf-8") as f:
            data_1 = yaml.safe_load(f)
        with open(path_2, "r", encoding="utf-8") as f:
            data_2 = yaml.safe_load(f)

    return mapping(data_1), mapping(data_2)


def mapping(data):
    for k, v in data.items():
        if v is None:
            data[k] = 'null'
        if v in (True, False):
            data[k] = str(v).lower()
    return data