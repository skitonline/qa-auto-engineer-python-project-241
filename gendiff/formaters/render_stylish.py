def to_stylish(all_data, diff_dict):
    result = []

    for k in all_data:
        if k in diff_dict['add'].keys():
            result.append(f"  + {k}: {diff_dict['add'][k]}")
        if k in diff_dict['remove'].keys():
            result.append(f"  - {k}: {diff_dict['remove'][k]}")
        if k in diff_dict['change'].keys():
            result.append(f"  - {k}: {diff_dict['change'][k][0]}")
            result.append(f"  + {k}: {diff_dict['change'][k][1]}")
        if k in diff_dict['equal'].keys():
            result.append(f"    {k}: {diff_dict['equal'][k]}")

    return '{\n' + '\n'.join(result) + '\n}'