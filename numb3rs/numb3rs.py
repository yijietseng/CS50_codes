import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    try:
        if match := re.search(r'([0-9]{0,3})\.([0-9]{0,3})\.([0-9]{0,3})\.([0-9]{0,3})', ip):
            a = int(match.group(1))
            b = int(match.group(2))
            c = int(match.group(3))
            d = int(match.group(4))
            if a <= 255 and b <= 255 and c <= 255 and d <= 255:
                return True
            else:
                return False
        else:
            return False
    except (TypeError, ValueError):
        return False



if __name__ == "__main__":
    main()