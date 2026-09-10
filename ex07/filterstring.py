import sys


def main():
    """Filter string elements with len superior to the given argument"""
    if len(sys.argv) != 3:
        raise AssertionError("Wrong number of arguments")

    if not isinstance(sys.argv[1], str):
        raise AssertionError("The arguments are bad")

    try:
        n = int(sys.argv[2])
    except ValueError:
        raise AssertionError("The arguments are bad")

    words = sys.argv[1].split()
    result = [word for word in words if (lambda x: len(x) > n)(word)]
    print(result)


if __name__ == "__main__":
    main()
