import requests
import sys


try:
    if (len(sys.argv) == 1):
        print("Missing command-line argument")
        sys.exit(1)
    elif float(sys.argv[1]) < 0:
        sys.exit(1)
except ValueError:
    print("Command-line argument is not a number ")
    sys.exit(1)

cont = float(sys.argv[1])

try:
    respons = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = respons.json()

    usd_rate = o['bpi']['USD']['rate_float']

    rez = cont * usd_rate
    print(f"${rez:,.4f}")


except requests.RequestException:
    ...
