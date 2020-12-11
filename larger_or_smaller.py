#!/usr/bin/env python3

# Created by Sean McLeod
# Created on December 2020
# This program can tell the user what number is larger or smaller, or if both
#    numbers are equal to each other


def main():
    # this function can determine what number is larger and smaller, or if
    #    both numbers are equal to each other

    print("This program can figure out what number is larger or smaller, "
          "or if they are equal.")
    print("\n", end="")

    # input
    first_string = input("Type in your first number: ")
    second_string = input("Type in your second number: ")
    print("\n", end="")

    # process & output
    try:
        first_number = int(first_string)
        second_number = int(second_string)

        if first_number > second_number:
            print("{0} is larger than {1}".format(first_number, second_number))
        elif second_number > first_number:
            print("{0} is larger than {1}".format(second_number, first_number))
        else:
            print("They are equal to each other")

    except Exception:
        print("This is not a number!")


if __name__ == "__main__":
    main()
