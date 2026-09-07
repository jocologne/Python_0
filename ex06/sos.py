import sys


def main():
    """Cypher string to morse code"""
    MORSE = {
     "A": ".-", "a": ".-",
     "B": "-...", "b": "-...",
     "C": "-.-.", "c": "-.-.",
     "D": "-..", "d": "-..",
     "E": ".", "e": ".",
     "F": "..-.", "f": "..-.",
     "G": "--.", "g": "--.",
     "H": "....", "h": "....",
     "I": "..", "i": "..",
     "J": ".---", "j": ".---",
     "K": "-.-", "k": "-.-",
     "L": ".-..", "l": ".-..",
     "M": "--", "m": "--",
     "N": "-.", "n": "-.",
     "O": "---", "o": "---",
     "P": ".--.", "p": ".--.",
     "Q": "--.-", "q": "--.-",
     "R": ".-.", "r": ".-.",
     "S": "...", "s": "...",
     "T": "-", "t": "-",
     "U": "..-", "u": "..-",
     "V": "...-", "v": "...-",
     "W": ".--", "w": ".--",
     "X": "-..-", "x": "-..-",
     "Y": "-.--", "y": "-.--",
     "Z": "--..", "z": "--..",
     "0": "-----",
     "1": ".----",
     "2": "..---",
     "3": "...--",
     "4": "....-",
     "5": ".....",
     "6": "-....",
     "7": "--...",
     "8": "---..",
     "9": "----.",
     " ": "/"
    }

    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return

    string = sys.argv[1]

    if not all(char.isalnum() or char == " " for char in string):
        print("AssertionError: the arguments are bad")
        return

    result = []
    for let in string:
        result.append(MORSE[let])
    print(" ".join(result))


if __name__ == "__main__":
    main()
