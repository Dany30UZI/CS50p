import requests
import sys


try:
    if (sys.argv) == 1:
        print("Missing command-line argument")
        sys.exit()
    elif (float(sys.argv[1]) < 0.0):
        sys.exit()
except ValueError:
    print("Command-line argument is not a number ")
    sys.exit()


try:
    ...
except requests.RequestException:
    ...
