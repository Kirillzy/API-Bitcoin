import requests
import sys
import json

try:
    if len(sys.argv) == 2 and not sys.argv[1].isalpha():
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        price = data["bpi"]["USD"]["rate_float"]
        amount = float(price) * float(sys.argv[1])
        print(f"${amount:,.4f}")
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")
    elif len(sys.argv) > 2:
        sys.exit("Too much Command-line arguements")
    else:
        sys.exit("Missing command-line argument")
except requests.RequestException:
    print("Error")

