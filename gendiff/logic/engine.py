from gendiff.logic.diff_builder import to_diff_dict
from gendiff.parsers.file_readers import parse_files
from gendiff.formaters.render_json import to_json
from gendiff.formaters.render_plain import to_plain
from gendiff.formaters.render_stylish import to_stylish


def generate_diff(path_1, path_2, format='stylish'):
    data_1, data_2 = parse_files(path_1, path_2)

    RENDERERS = {
        "stylish": to_stylish,
        "plain": to_plain,
        "json": to_json,
    }
    render = RENDERERS.get(format)

    diff_dict = to_diff_dict(data_1, data_2)
    all_data = sorted(data_1.keys() | data_2.keys())
    
    return render(all_data, diff_dict)



    