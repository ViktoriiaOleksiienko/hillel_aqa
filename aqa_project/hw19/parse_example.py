from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('--a', help='first argument to parse', default=5)
parser.add_argument('--b', help='second argument to parse', default=6)
args = parser.parse_args()
a = args.a
b = args.b
print(a+b)