import sys


def doubleit(x):
    return int(x) * 2

if __name__ == '__main__':
    input_val = sys.argv[1]
    double_val = doubleit(input_val)

    print("the value of {original} is {doubled}".format(original=input_val, doubled=double_val))
