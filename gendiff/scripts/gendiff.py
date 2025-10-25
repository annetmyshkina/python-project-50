from gendiff.generate_diff import generate_diff
from gendiff.parser import parser_args


def main():
    args = parser_args()
    data1 = args.first_file
    data2 = args.second_file
    format_name = args.format
    diff = generate_diff(data1, data2, format_name)
    print(diff)


if __name__ == "__main__":
    main()