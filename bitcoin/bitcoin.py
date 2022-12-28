import requests, sys
from sys import argv


def main():
    No_bit = get_bitN()
    amount = cal_bit_value(No_bit)
    print(amount)


def get_bitN():
    if len(argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(argv) >= 2:
        try:
            bit_N = float(argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
    return bit_N

def cal_bit_value(No_bit):
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r_json = r.json()
    bit_value = r_json["bpi"]["USD"]["rate_float"]
    total = No_bit * bit_value

    return f"${total:,.4f}"


if __name__ == "__main__":
    main()
