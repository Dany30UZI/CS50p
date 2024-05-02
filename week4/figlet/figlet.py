import pyfiglet
import sys
import random

try:
    if len(sys.argv) == 1:
        fig = pyfiglet.Figlet()
        c = input("Input: ")
        result = pyfiglet.figlet_format(c, font = random.choice(fig.getFonts()))
        print("Output:")
        print(result)
    elif len(sys.argv) == 3:
        c = input("Input: ")
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            result = pyfiglet.figlet_format(c, font = sys.argv[2])
            print("Output:")
            print(result)
    else:
        print("Invalid usage")
except Exception as e:
    print("Invalid usage")



