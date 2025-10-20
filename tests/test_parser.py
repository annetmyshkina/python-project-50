from gendiff.parser import parser_args

def test_parser_args_basic():
    args = parser_args(['file1.json', 'file2.json'])
    assert args.first_file == 'file1.json'
    assert args.second_file == 'file2.json'
    assert args.format == 'stylish'

def test_parser_args_with_format():
    args = parser_args(['file1.json', 'file2.json', '--format', 'plain'])
    assert args.format == 'plain'