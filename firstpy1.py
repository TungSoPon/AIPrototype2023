import argparse

def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--num',
        type=int,
        default=7,
        help='input for the multiplyby9 function'
    )

    parser.add_argument(
        '--XX',
        type=int,
        default=7,
        help='input for XX'
    )

    args = parser.parse_args()
    return args

def printHello():
    print("Hello World")

def multiplyby9(inputV):
    print(9 * inputV)

if __name__ == "__main__":
    input_args = parse_input()
    print(f'the input num is {input_args.num}')
    print(f'the input XX is {input_args.XX}')
    print('we are in the main function')
    multiplyby9(input_args.num)
    multiplyby9(input_args.XX)
    printHello()

