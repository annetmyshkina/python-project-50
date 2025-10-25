import json


def get_json(tree_diff):
    json_string = json.dumps(tree_diff, indent=4)
    return json_string