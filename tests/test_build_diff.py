import pytest
from gendiff.build_diff import build_diff


@pytest.mark.parametrize(
    "data1, data2, expected",
    [
        (
                {"key1": "value1"},
                {"key1": "value1"},
        [
                    {
                        "key": "key1",
                        "status": "unchanged",
                        "value": "value1"
                    }
                    ]
        ),
        (
                {"key1": "value1"},
                {"key1": "value2"},
        [
                    {"key": "key1",
                     "status": "changed",
                     "old_value": "value1",
                     "new_value": "value2"
                     }
                ]
        ),
        (
                {}, {"key2": "value2"},
            [
                {
                    "key": "key2",
                    "status": "added",
                    "value": "value2"
                }
            ]
        ),
        (
                {"key3": "value3"}, {},
            [
                {
                    "key": "key3",
                    "status": "deleted",
                    "value": "value3"
                }
            ]
        ),
        (
                {"key4": {"k1": 1, "k2": 2}},
                {"key4": {"k1": 3, "k2": 4}},
            [
               {
                   "key": "key4",
                   "status": "nested",
                   "children":
                    [
                        {
                            "key": "k1",
                            "status": "changed",
                            "old_value": 1,
                            "new_value": 3
                        },
                        {
                            "key": "k2",
                            "status": "changed",
                            "old_value": 2,
                            "new_value": 4
                        }
                    ]
                }
            ]
        ),
        (
                {"key5": {"k1": 1, "k2": 2}},
                {},
                [
                    {
                        "key": "key5",
                        "status": "deleted",
                        "value": {"k1": 1, "k2": 2}
                    }
                ]
        )
    ]
)
def test_build_diff(data1, data2, expected):
    result = build_diff(data1, data2)

    assert result == expected
    assert isinstance(result, list)
