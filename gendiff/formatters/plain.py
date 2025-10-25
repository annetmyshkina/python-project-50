def to_str(value):
    if isinstance(value, (dict, list)):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return f"'{str(value)}'"


def get_plain(tree_diff, full_path=None):
    lines = []
    if full_path is None:
        full_path = []
    for item in tree_diff:
        status = item["status"]
        current_path = full_path + [item["key"]]
        if status == "nested":
            children = get_plain(item["children"], current_path)
            lines.append(children)
        elif status == 'added':
            value = to_str(item['value'])
            lines.append(
                f"Property '{'.'.join(current_path)}' "
                f"was added with value: {value}")
        elif status == 'deleted':
            lines.append(f"Property '{'.'.join(current_path)}' was removed")
        elif status == 'changed':
            old_value = to_str(item['old_value'])
            new_value = to_str(item['new_value'])
            lines.append(
                f"Property '{'.'.join(current_path)}' was updated. "
                f"From {old_value} to {new_value}"
            )
    return '\n'.join(lines)