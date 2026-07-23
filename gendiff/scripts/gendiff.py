from gendiff.cli_processing import parsing
from gendiff.engine import generate_diff

PATH_1 = "assets/file1.json"
PATH_2 = "assets/file2.json"


def main():
    args = parsing()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "__main__":
    main()
