import json

PATH_1 = "assets/file1.json"
PATH_2 = "assets/file2.json"


def generate_diff(path_1=PATH_1, path_2=PATH_2):
    data_1 = json.load(open(path_1))
    data_2 = json.load(open(path_2))

    all_data = sorted(set(data_1.keys()) | set(data_2.keys()))

    result = []
    for k in all_data:
        if k in data_1.keys() and k in data_2.keys() and data_1[k] == data_2[k]:
            result.append(f"   {k}: {data_1[k]}")
        else:
            if k in data_1:
                result.append(f" - {k}: {data_1[k]}")
            if k in data_2:
                result.append(f" + {k}: {data_2[k]}")

    result = "{\n" + "\n".join(result) + "\n}"
    return result
