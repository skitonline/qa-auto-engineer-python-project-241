def to_diff_dict(data_1, data_2):
    union = data_1.keys() & data_2.keys()
    minus_1_and_2 = data_1.keys() - data_2.keys()
    minus_2_and_1 = data_2.keys() - data_1.keys()

    result = {
        'add': {k: data_2[k] for k in minus_2_and_1},
        'remove': {k: data_1[k] for k in minus_1_and_2},
        'change': {},
        'equal': {}
    }

    for k in union:
        if data_1[k] == data_2[k]:
            result['equal'][k] = data_1[k]
        else:
            result['change'][k] = (data_1[k], data_2[k])

    return result