import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):

    share = 'https://youtu.be/'
    if m := re.search(r'https?://(?:www\.)?youtube\.com/embed/(\w+)\"', s):
        share_code = m.group(1)
        combine = share+share_code
        return combine
    else:
        return None


if __name__ == "__main__":
    main()