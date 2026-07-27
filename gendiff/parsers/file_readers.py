import json
from pathlib import Path

import yaml


def parse_files(path_1, path_2):
    format_file_1 = Path(path_1).suffix
    format_file_2 = Path(path_2).suffix

    yamls = (".yaml", ".yml")
    if format_file_1 in yamls and format_file_2 in yamls:
        format_file_1 = format_file_2 = '.yaml'

    if format_file_1 != format_file_2:
        raise ValueError(f"Different files format: \
{format_file_1} and {format_file_2}")

    if format_file_1 == ".json":
        data_1 = json.load(open(path_1))
        data_2 = json.load(open(path_2))
    elif format_file_1 == ".yaml":
        with open(path_1, "r", encoding="utf-8") as f:
            data_1 = yaml.safe_load(f) or {}
        with open(path_2, "r", encoding="utf-8") as f:
            data_2 = yaml.safe_load(f) or {}
    else:
        raise ValueError(f"Unsupported file format: {format_file_1}")

    return to_files_format(data_1), to_files_format(data_2)


def to_files_format(data):
    for k, v in data.items():
        if v is None:
            data[k] = 'null'
        if v in (True, False):
            data[k] = str(v).lower()
    return data