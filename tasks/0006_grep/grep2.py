# Write your code for Task 2 here.
import sys
import argparse


parser = argparse.ArgumentParser(description="Grep functions with argparse module")
parser.add_argument("text", type=str, help="Text for search in file")
parser.add_argument("filename", type=str, help="File for read")

group = parser.add_mutually_exclusive_group()
group.add_argument(
    "-i", "--ignore-case", action="store_true", help="ignore pattern case"
)
group.add_argument(
    "-c", "--count", action="store_true", help="output matched lines count instead of the matched lines"
)
group.add_argument(
    "-n", "--line-number", action="store_true", help="output line numbers in front of matched lines"
)
group.add_argument(
    "-v", "--invert-search", action="store_true", help="output the lines which do NOT match the pattern"
)

args = parser.parse_args()


class Options:
    def __init__(self, arguments):
        self.ignore_case = args.ignore_case
        self.show_count = args.count
        self.show_line_number = args.line_number
        self.invert_search = args.invert_search


def main():
    options = Options(sys.argv)

    if len(sys.argv) < 3:
        print(f"Usage: python {sys.argv[0]} [OPTION] text filename")
        exit(0)

    filename = args.filename
    text = args.text

    count = 0

    with open(filename, "r") as f:
        for line_number, line in enumerate(f, start=1):
            grep_result = do_line_grep(text, line, options, line_number)

            if grep_result is None:
                continue

            count += 1
            if not options.show_count:
                print(grep_result)

        if options.show_count:
            print(count)


def do_line_grep(text, line, options, line_number):
    match = False

    if options.ignore_case:
        match = text.lower() in line.lower()
    elif options.invert_search:
        match = text not in line
    else:
        match = text in line

    if match:
        if options.show_line_number:
            return f"{line_number}: {line.rstrip()}"
        else:
            return line.rstrip()


if __name__ == "__main__":
    main()
