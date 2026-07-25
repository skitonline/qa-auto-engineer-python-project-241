import json


def to_json(all_data, diff_dict):
    result = []

    for k in all_data:
        if k in diff_dict['add'].keys():
            result.append({
                "key": k,
                "type": "added",
                "value": diff_dict['add'][k],
            })
        if k in diff_dict['remove'].keys():
            result.append({
                "key": k,
                "type": "removed",
                "value": diff_dict['remove'][k],
            })
        if k in diff_dict['change'].keys():
            old, new = diff_dict['change'][k]
            result.append({
                "key": k,
                "type": "changed",
                "old_value": old,
                "new_value": new,
            })

    return json.dumps(result, indent=2)
