import requests
import sys
import json

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing Command-Line Argument")

    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-Line Argument is not a number")

    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    if request.status_code != 200:
        sys.exit("Failed to retrieve data")

    data = request.json()
    rate = data["bpi"]["USD"]["rate_float"]
    total_price = amount * rate
    print(f"${total_price:,.4f}")

if __name__ == "__main__":
    main()
