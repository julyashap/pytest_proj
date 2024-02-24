from utils import arrs
import pytest

@pytest.fixture
def test_data1():
    return [1, 2, 3]

@pytest.fixture
def test_data2():
    return [1, 2, 3, 4]

@pytest.fixture
def test_data3():
    return []


def test_get(test_data1, test_data3):
    assert arrs.get(test_data1, 1, "test") == 2
    assert arrs.get(test_data3, 0, "test") == "test"


def test_slice(test_data1, test_data2):
    assert arrs.my_slice(test_data2, 1, 3) == [2, 3]
    assert arrs.my_slice(test_data1, 1) == [2, 3]

def test_slice_empty_list(test_data3):
    assert arrs.my_slice(test_data3, 0, 0) == []

def test_slice_no_start(test_data1):
    assert arrs.my_slice(test_data1, end=1) == [1]
