from unittest.mock import _ArgsKwargs
import argparse
from unittest.mock import _ArgsKwargs

def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--num',
        type=int,
        required=True,
        help='input for the multiplyby9 funtion'
    )

    args = parser.parse_arge()
    return _ArgsKwargs

def printHello():
    print("Hello World")

def multiplyby9(inputV):
    print(9*inputV)

if __name__== "__main__":
    input_v = parse_input()
    print(f'the input num is {input_v.num}')
    print('we are in the main funtion')
    multiplyby9(20)
    printHello()