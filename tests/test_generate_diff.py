import pytest

from gendiff.logic.engine import generate_diff


@pytest.fixture
def path_1():
    return 'tests/test_data/input/file1.json'


@pytest.fixture
def path_2():
    return 'tests/test_data/input/file2.json'


def test_stylish(path_1, path_2):
    with open('tests/test_data/output/stylish.txt', "r", encoding="utf-8") as f:
        result = f.read()
    assert generate_diff(path_1, path_2) == result


def test_plain(path_1, path_2):
    with open('tests/test_data/output/plain.txt', "r", encoding="utf-8") as f:
        result = f.read()
    assert generate_diff(path_1, path_2, 'plain') == result


def test_json(path_1, path_2):
    with open('tests/test_data/output/json.txt', "r", encoding="utf-8") as f:
        result = f.read()
    assert generate_diff(path_1, path_2, 'json') == result