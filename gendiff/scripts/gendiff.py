from gendiff.args import parsing
from gendiff.engine import generate_diff


def main():
    args = parsing()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
