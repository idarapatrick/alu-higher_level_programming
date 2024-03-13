#!/usr/bin/python3
# Prints the number of and the list of its arguments

if __name__ == "__main__":
    import sys
    arguments = sys.argv
    number_of_arguments = len(arguments) - 1
    if number_of_arguments == 1:
        print(f"{number_of_arguments} argument.")
    elif number_of_arguments == 0:
        print(f"{number_of_arguments} arguments.")
    else:
        print(f"{number_of_arguments} arguments:")

    for arg in range(len(arguments)):
        if arg > 0:
            print("{}: {}".format(arg, arguments[arg]))