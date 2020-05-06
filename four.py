"""
    In this problem you will open a file (four.txt), you will read some information from the file
    then you will right a output of that information to a new file solution4.txt
    1) On every line of the file input there is a character that is uppper or lower when
    the other characters are the opposite
    Concatenate all of these characters to build a message.
    2) Sum all of the numbers on the first 10 lines, call this final number J
       Split the 11th line on the most frequent character
       the word at the Jth position can be called the Fword
       Return the number of times that the Fword appears in the file case insensitive.
    3) In solution4.txt output on the first line the message, the next line the frequency
    Example solution4.txt:
    "Hidden Message"
    34

"""


def performCalculations(value):
    result = f3(f1((f2(f2(f2(f2(value, value),value),value),value)), value), f2(f2(f1(value, f3(f2(f2(f1(value, value), f1(value, value)), f1(value, value)),value)), value), value))
    return result
 
def f1(v1, v2):
    return v1 // v2


def f2(v3, v4):
    return v4 + v3


def f3(v1, v2):
    return v2 - v1


def f4(v):
    return v * v


def f5(v1, v2):
    return v1 / v2


def tester(input, output):
    actual_result = performCalculations(input)
    expected_result = output
    print_text = "In: " + str(input) + " | "
    if expected_result == actual_result:
        print_text += "Correct: " + str(expected_result) + " == " + str(actual_result)
    else:
        print_text += "Incorrect: " + str(expected_result) + " != " + str(actual_result)
    return print_text


if __name__ == "__main__":
    print(tester(350, 696))
    print(tester(37, 70))
    print(tester(-40, -85))
    print(tester(-2, -9))
    print(tester(15, 26))
