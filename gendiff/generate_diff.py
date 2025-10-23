import json
import yaml
import os

from gendiff.build_diff import build_diff
from gendiff.formatters import stylish, plain

def reader_file(filepath):
    extension = os.path.splitext(filepath)[1].lower()
    with open(filepath, 'r') as f:
        if extension in ('.yaml', '.yml'):
            return yaml.safe_load(f)
        elif extension == '.json':
            return json.load(f)
        else:
            raise ValueError(f'Unsupported file format {extension}')

def generate_diff(filepath1, filepath2, format_name='stylish'):
    data1 = reader_file(filepath1)
    data2 = reader_file(filepath2)
    tree_diff = build_diff(data1, data2)

    formatters = {
        "stylish": stylish,
        "plain": plain,
    }

    formater = formatters.get(format_name, stylish)
    return formater(tree_diff)
