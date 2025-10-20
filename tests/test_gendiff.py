import json
from pathlib import Path
from gendiff.find_diff import generate_diff


def read_file(filepath):
    return Path(filepath).read_text()


def test_json_diff():
    data1_path = 'tests/test_data/data1.json'
    data2_path = 'tests/test_data/data2.json'
    expected_path = 'tests/test_data/result.txt'

    data1 = json.loads(read_file(data1_path))
    data2 = json.loads(read_file(data2_path))
    expected = read_file(expected_path).strip()

    result = generate_diff(data1, data2).strip()

    assert result == expected

def test_key_only_in_first():
    data1 = {'key1': 'value1'}
    data2 = {}
    expected = "{\n  - key1: value1\n}"
    assert generate_diff(data1, data2) == expected

def test_key_only_in_second():
    data1 = {}
    data2 = {'key1': 'value1'}
    expected = "{\n  + key1: value1\n}"
    assert generate_diff(data1, data2) == expected

def test_identical_keys():
    data1 = {'key1': 'value1'}
    data2 = {'key1': 'value1'}
    expected = "{\n    key1: value1\n}"
    assert generate_diff(data1, data2) == expected
