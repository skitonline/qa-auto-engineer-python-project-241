def to_plain(all_data, diff_dict):
    result = []

    for k in all_data:
        if k in diff_dict['add'].keys():
            result.append(f"Property '{k}' was added \
with value: {diff_dict['add'][k]}")
        if k in diff_dict['remove'].keys():
            result.append(f"Property '{k}' was removed")
        if k in diff_dict['change'].keys():
            result.append(f"Property '{k}' was updated. \
From {diff_dict['change'][k][0]} to {diff_dict['change'][k][1]}")

    return '\n'.join(result)