from gendiff.generate_diff import generate_diff


expected_path = 'tests/test_data/result.txt'
with open(expected_path, 'r', encoding="utf-8") as file:
    expected = file.read().strip()


def test_json_diff():
    data1_path = 'tests/test_data/data1.json'
    data2_path = 'tests/test_data/data2.json'
    result = generate_diff(data1_path, data2_path, format_name='stylish')

    assert isinstance(result, str)
    assert result == expected
    assert len(result) > 0


def test_yml_diff():
    data1_path = 'tests/test_data/YML_data1.yml'
    data2_path = 'tests/test_data/YML_data2.yaml'
    result = generate_diff(data1_path, data2_path, format_name='stylish')

    assert isinstance(result, str)
    assert result == expected
    assert len(result) > 0
