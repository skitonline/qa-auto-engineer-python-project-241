from gendiff.diff_dict import to_diff_dict
from gendiff.files_to_dict import files_to_dicts
from gendiff.formaters.render_json import to_json
from gendiff.formaters.render_plain import to_plain
from gendiff.formaters.render_stylish import to_stylish


def generate_diff(path_1, path_2, format):
    data_1, data_2 = files_to_dicts(path_1, path_2)

    RENDERERS = {
        "stylish": to_stylish,
        "plain": to_plain,
        "json": to_json,
    }
    render = RENDERERS.get(format)

    diff_dict = to_diff_dict(data_1, data_2)
    all_data = sorted(data_1.keys() | data_2.keys())
    
    return render(all_data, diff_dict)



    