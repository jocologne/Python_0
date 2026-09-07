import sys


def main():
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    if not isinstance(sys.argv[1], str):
        print("AssertionError: the arguments are bad")
        return

    try:
        n = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    words = sys.argv[1].split()
    result = [word for word in words if (lambda x: len(x) > n)(word)]
    print(result)


if __name__ == "__main__":
    main()
