#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    n = len(sys.argv) - 1
    operators = ["+", "-", "*", "/"]
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        if sys.argv[2] not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            if sys.argv[2] == operators[0]:
                a = int(sys.argv[1])
                b = int(sys.argv[3])
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif sys.argv[2] == operators[1]:
                a = int(sys.argv[1])
                b = int(sys.argv[3])
                print("{} - {} = {}".format(a, b, sub(a, b)))
            elif sys.argv[2] == operators[2]:
                a = int(sys.argv[1])
                b = int(sys.argv[3])
                print("{} * {} = {}".format(a, b, mul(a, b)))
            else:
                a = int(sys.argv[1])
                b = int(sys.argv[3])
                print("{} / {} = {}".format(a, b, div(a, b)))
