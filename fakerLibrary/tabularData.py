import argparse

if __name__ == '__main__':
    # Initialization
    parser = argparse.ArgumentParser(description='Mathematics Crash Course!')

    # positional and optional Parameter
    parser.add_argument('number1', help=' enter first number', type=int)
    parser.add_argument('number2', help=' enter second number', type=int)
    parser.add_argument('--operator', help=' enter operator', default='+')
    # parser.add_argument('textOne', help=' enter a text of your choice', type=str)
    # parser.add_argument('--textTwo', help=' enter another text of your choice', type=str)

    # args = parser.parse_args()
    result = None
    # Parse the arguments
    args = parser.parse_args()
    if args.operator == '+':
        result = args.number1 + args.number2
    elif args.operator == '-':
        result = args.number1 - args.number2
    elif args.operator == '*':
        result = args.number1 * args.number2
    elif args.operator == '/':
        result = args.number1 / args.number2
    elif args.operator == '%':
        result = args.number1 % args.number2
    else:
        result = 0

    print(result)
    # print(args.textOne)
    # print(args.textTwo)
