import json
from pathlib import Path

import yaml


def parse_files(path_1, path_2):
    format_file_1 = Path(path_1).suffix
    format_file_2 = Path(path_2).suffix

    data_1 = read_file(path_1, format_file_1)
    data_2 = read_file(path_2, format_file_2)

    return to_files_format(data_1), to_files_format(data_2)


def read_file(path, format):
    if format == '.json':
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    elif format in (".yaml", ".yml"):
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    else:
        raise ValueError(f"Unsupported file format: {format}")


def to_files_format(data):
    for k, v in data.items():
        if v is None:
            data[k] = 'null'
        if v in (True, False):
            data[k] = str(v).lower()
    return data