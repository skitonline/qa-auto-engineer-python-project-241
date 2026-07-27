from gendiff.logic.diff_builder import to_diff_dict


def test_diff_builder_equal_dicts():
    d1 = {"host": "localhost", "port": 8080}
    d2 = {"host": "localhost", "port": 8080}

    diff = to_diff_dict(d1, d2)

    assert not diff["add"]
    assert not diff["remove"]
    assert not diff["change"]
    assert "host" in diff["equal"]
    assert "port" in diff["equal"]


def test_diff_builder_key_added():
    d1 = {"host": "localhost"}
    d2 = {"host": "localhost", "port": 8080}

    diff = to_diff_dict(d1, d2)

    assert diff["add"]["port"] == 8080
    assert not diff["remove"]
    assert not diff["change"]


def test_diff_builder_key_removed():
    d1 = {"host": "localhost", "port": 8080}
    d2 = {"host": "localhost"}

    diff = to_diff_dict(d1, d2)

    assert diff["remove"]["port"] == 8080
    assert not diff["add"]
    assert not diff["change"]


def test_diff_builder_value_changed():
    d1 = {"host": "localhost", "port": 8080}
    d2 = {"host": "example.com", "port": 8080}

    diff = to_diff_dict(d1, d2)

    old, new = diff["change"]["host"]
    assert old == "localhost"
    assert new == "example.com"


def test_diff_builder_empty_dicts():
    d1 = {}
    d2 = {}

    diff = to_diff_dict(d1, d2)

    assert not diff["add"]
    assert not diff["remove"]
    assert not diff["change"]
    assert not diff["equal"]
