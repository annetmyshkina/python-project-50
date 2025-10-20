from typing import Any


def generate_diff(data1: dict[str, Any], data2: dict[str, Any]):
    base_keys = sorted(set(data1.keys()) | set(data2.keys()))
    result = ['{']

    for key in base_keys:
        in_first = key in data1
        in_second = key in data2
        if in_first and not in_second:
            result.append(f'  - {key}: {data1[key]}')
        if not in_first and in_second:
            result.append(f'  + {key}: {data2[key]}')
        if in_first and in_second:
            if data1[key] == data2[key]:
                result.append(f'    {key}: {data1[key]}')
            else:
                result.append(f'  - {key}: {data1[key]}')
                result.append(f'  + {key}: {data2[key]}')

    result.append('}')
    return '\n'.join(result)




