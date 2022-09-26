'''
exit 1 : Value error or Type error
'''

import sys


def check_string(num):
    try:
        int(num)
    except Exception as e:
        print("Must be a binary number (contain only 1s and 0s)")
        sys.exit(1)


def check_decimal(num):
    try:
        decimal = int(num, 2)
        return decimal
    except Exception as e:
        print("Must be a binary number (contain only 1s and 0s)")
        sys.exit(1)

def validate_binary(decimal):
    if 0 <= decimal <= 16:
        pass
    else:
        print("Entered number is out of range")
        sys.exit(1)


### Returns '0' for '1' and '1' for '0'
def reverse_bin(val):
    if val == '0':
        return '1'
    else:
        return '0'


def ones_complement(num):
    n = len(num)
    ones = ""
    # for ones complement flip every bit
    for i in range(n):
        ones += reverse_bin(num[i])
    print(f"The one's complement  is {ones}")


if __name__ == '__main__':
    num = input("Enter a Binary number between 0 and 10000: ")
    check_string(num)
    decimal = check_decimal(num)
    validate_binary(decimal)
    ones_complement(num)

