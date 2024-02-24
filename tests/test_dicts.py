from utils import dicts

def test_dicts():
    assert dicts.get_val({1:"one", 2:"two"}, 2) == "two"
    assert dicts.get_val({1:"one", 2:"two"}, 2, "git") == "two"
    assert dicts.get_val({}, "key", "no") == "no"
    assert dicts.get_val({}, "key") == "git"
