import pytest

from gendiff.parsers.file_readers import parse_files


@pytest.fixture
def data_1():
    return {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": "false",
        "null is": "null"
    }


@pytest.fixture
def data_2():
    return {
        "timeout": 20,
        "verbose": 'true',
        "host": "hexlet.io",
        "null is": "null"
    }


def test_json_files(data_1, data_2):
    path_1 = 'tests/test_data/input/file1.json'
    path_2 = 'tests/test_data/input/file2.json'
    assert parse_files(path_1, path_2) == (data_1, data_2)


def test_yaml_files(data_1, data_2):
    path_1 = 'tests/test_data/input/file1.yaml'
    path_2 = 'tests/test_data/input/file2.yaml'
    assert parse_files(path_1, path_2) == (data_1, data_2)


def test_yml_files(data_1, data_2):
    path_1 = 'tests/test_data/input/file1.yml'
    path_2 = 'tests/test_data/input/file2.yml'
    assert parse_files(path_1, path_2) == (data_1, data_2)


def test_yaml_and_yml_files(data_1, data_2):
    path_1 = 'tests/test_data/input/file1.yml'
    path_2 = 'tests/test_data/input/file2.yaml'
    assert parse_files(path_1, path_2) == (data_1, data_2)


def test_wrong_format():
    path_1 = 'tests/test_data/input/file1.yml'
    path_2 = 'tests/test_data/input/wrong_format.txt'
    with pytest.raises(ValueError):
        parse_files(path_1, path_2)


def test_different_formats():
    path_1 = 'tests/test_data/input/file1.yml'
    path_2 = 'tests/test_data/input/file1.json'
    with pytest.raises(ValueError):
        parse_files(path_1, path_2)


def test_empty_json(data_1):
    path_1 = 'tests/test_data/input/file1.json'
    path_2 = 'tests/test_data/input/empty.json'
    assert parse_files(path_1, path_2) == (data_1, {})


def test_empty_yaml(data_1):
    path_1 = 'tests/test_data/input/file1.yaml'
    path_2 = 'tests/test_data/input/empty.yaml'
    assert parse_files(path_1, path_2) == (data_1, {})