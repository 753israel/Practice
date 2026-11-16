from pathlib import Path
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-l",action="store_true")
parser.add_argument("--sort",action="store_true")
# parser.add_argument("-x", "--extension", default=["txt"], nargs="*")  # 0 or more


args = parser.parse_args()

print(args)

files = ["1.txt", "z.exe", "b.pdf", "y.exe", "2.txt"]

if args.sort:
    files.sort()

if args.l:
    for i in files:
        print(i)

else:
    for i in files:
        print(i,end=" ")
    print()













# group = parser.add_argument_group("Image size")
# group.add_argument("--width")
# group.add_argument("--height")
# group2 = parser.add_mutually_exclusive_group()
# group2.add_argument("--width")
# group2.add_argument("--height")