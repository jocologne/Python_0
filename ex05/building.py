import sys


def main():
    """Count characters in string"""

    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    if len(sys.argv) == 1:
        string = input("What is the text to count?\n")
    else:
        string = sys.argv[1]

    let = len(string)
    upper = 0
    lower = 0
    punc = 0
    space = 0
    dig = 0

    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isspace():
            space += 1
        elif char.isdigit():
            dig += 1
        else:
            punc += 1

    print("The text contains", let, "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punc, "punctuation marks")
    print(space, "spaces")
    print(dig, "digits")


if __name__ == "__main__":
    main()
