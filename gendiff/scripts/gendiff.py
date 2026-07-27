from gendiff.logic.engine import generate_diff
from gendiff.parsers.args import parsing


def main():
    args = parsing()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
