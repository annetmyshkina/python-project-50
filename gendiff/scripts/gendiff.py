import json

from gendiff.find_diff import generate_diff
from gendiff.parser import parser_args


def reader_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def main():
    args = parser_args()
    data1 = reader_file(args.first_file)
    data2 = reader_file(args.second_file)
    diff = generate_diff(data1, data2)
    print(diff)


if __name__ == "__main__":
    main()