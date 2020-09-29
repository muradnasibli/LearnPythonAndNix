# Write your code for Task 1 here.
import sys


# [-c], [-n] options working with this method
def text_in_file(text, filename):
    line_number = 0
    list_of_results = []
    with open(filename, "r") as read_file:
        # Read all lines in the file one by one
        for line in read_file:
            line_number += 1
            if text in line:
                # Add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    return list_of_results


# [-i] ignore pattern case option method
def ignore_pattern_case(text, filename):
    line_number = 0
    list_of_results = []
    with open(filename, "r") as read_file:
        # Read all lines in the file one by one
        for line in read_file:
            line_number += 1
            if text.lower() in line.lower():
                # Add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    return list_of_results


# [-v] option working with this
def text_not_in_file(text, filename):
    line_number = 0
    list_of_results = []
    with open(filename, "r") as read_file:
        # Read all lines in the file one by one
        for line in read_file:
            line_number += 1
            if text not in line:
                # Add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    return list_of_results


def main():
    # my list with given options
    mylist = ["-i", "-n", "-v", "-c"]

    # [project name]  -[option] [text] [filename]
    # grep1.py -i info README.rst

    option = sys.argv[1]
    text = sys.argv[2]
    filename = sys.argv[3]

    for arg in sys.argv[1:2]:
        # Check does given option in list or not
        if mylist.__contains__(arg):
            for opt in mylist:
                # Check my first index of argument equals to
                if option == opt:
                    if opt == "-i":
                        matched = ignore_pattern_case(text, filename)
                        for elem in matched:
                            print(str(elem[1]))
                    elif opt == "-c":
                        matched = text_in_file(text, filename)
                        print(len(matched))
                    elif opt == "-n":
                        matched = text_in_file(text, filename)
                        for elem in matched:
                            print(str(elem[0]) + ": ", str(elem[1]))
                    elif opt == "-v":
                        matched = text_not_in_file(text, filename)
                        for elem in matched:
                            print(str(elem[1]))
                    else:
                        print("Patterns are not found!")
        else:
            print("This options not found in [mylist]")


if __name__ == "__main__":
    main()
