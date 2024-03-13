#!/usr/bin/python3
# Prints the number of and the list of its arguments

if __name__ == "__main__":
    import sys

    arguments = sys.argv
    number_of_arguments = len(arguments) - 1

    if number_of_arguments > 1:
        print(f"{number_of_arguments} arguments:")
        for i in range(1, number_of_arguments + 1):
            print(f"{i}: {arguments[i]}")

    elif number_of_arguments == 0:
        print(f"{number_of_arguments} arguments.")

    else:
        print(f"{number_of_arguments} argument:")
        print(f"{number_of_arguments}: {arguments[0]}")