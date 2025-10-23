def to_str(value, depth):
    indent = ' ' * (depth * 4)
    if isinstance(value, dict):
        lines = ['{']
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {to_str(v, depth + 1)}")
        lines.append(f"{indent}}}")
        return '\n'.join(lines)
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)


def stylish(tree_diff, depth=0):
    lines = ['{']
    indent = ' ' * (depth * 4)
    for item in tree_diff:
        key = item["key"]
        status = item["status"]
        if status == "nested":
            children = stylish(item["children"], depth + 1)
            lines.append(f'{indent}    {key}: {children}')
        elif status == 'added':
            value = to_str(item['value'], depth + 1)
            lines.append(f"{indent}  + {key}: {value}")
        elif status == 'deleted':
            val = to_str(item['value'], depth + 1)
            lines.append(f"{indent}  - {key}: {val}")
        elif status == 'changed':
            old_value = to_str(item['old_value'], depth + 1)
            new_value = to_str(item['new_value'], depth + 1)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")
        elif status == 'unchanged':
            val = to_str(item['value'], depth + 1)
            lines.append(f"{indent}    {key}: {val}")
    lines.append(f"{indent}}}")
    return '\n'.join(lines)
