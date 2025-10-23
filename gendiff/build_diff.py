from typing import Dict, Any

def build_diff(data1: Dict[str, Any], data2: Dict[str, Any]) -> list[Dict[str, Any]]:
    base_keys = sorted(set(data1) | set(data2))
    tree_diff = []

    for key in base_keys:
        if key not in data1:
            tree_diff.append({"key": key, "status": "added", "value": data2[key]})
        elif key not in data2:
            tree_diff.append({"key": key, "status": "deleted", "value": data1[key]})
        else:
            value1, value2 = data1[key], data2[key]
            if isinstance(value1, dict) and isinstance(value2, dict):
                children = build_diff(value1, value2)
                tree_diff.append({"key": key, "status": "nested", "children": children})
            elif value1 != value2:
                tree_diff.append({"key": key, "status": "changed", "old_value": value1, "new_value": value2})
            else:
                tree_diff.append({"key": key, "status": "unchanged", "value": value1})

    return tree_diff