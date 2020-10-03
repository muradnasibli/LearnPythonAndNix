# Write your code for Task 1 here.
import sys


class Options:
    def __init__(self, args):
        self.ignore_case = "-i" in args
        self.show_count = "-c" in args
        self.show_line_number = "-n" in args
        self.invert_search = "-v" in args


def main():
    options = Options(sys.argv)

    if len(sys.argv) < 3:
        print(f"Usage: python {sys.argv[0]} [OPTION] text filename")
        exit(0)

    filename = sys.argv[-1]
    text = sys.argv[-2]

    count = 0

    with open(filename, "r") as f:
        for line_number, line in enumerate(f, start=1):
            if options.show_count:
                if text in line:
                    count += 1
                    continue

            grep_result = do_line_grep(text, line, options, line_number)

            if grep_result is not None:
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
            return f"{line_number}: {line.rstrip()}"  # string interpolation instead of str(...) + '...' + str(...)
        else:
            return line.rstrip()


main()
