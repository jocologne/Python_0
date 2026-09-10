import sys


def main():
    if len(sys.argv) != 2:
        raise AssertionError("Incorrect number of arguments")

    try:
        number = int(sys.argv[1])
    except ValueError:
        raise AssertionError("Argument is not an integer")

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()
