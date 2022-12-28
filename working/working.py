import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    try:
        if m := re.search(r'([0-1]?\d)(?:\:([0-5]\d))? (AM|PM) to ([0-1]?\d)(?:\:([0-5]\d))? (AM|PM)',s):
            hr1 = int(m.group(1))
            if m.group(2) == None:
                min1 = 0
            else:
                min1 = int(m.group(2))
            ap1 = m.group(3)
            hr2 = int(m.group(4))
            if m.group(5) == None:
                min2 = 0
            else:
                min2 = int(m.group(5))
            ap2 = m.group(6)

            # convert to 24hr format
            if ap1 == 'PM':
                if int(hr1) != 12:
                    hr1 = int(hr1) + 12
            else:
                if int(hr1) == 12:
                    hr1 = 0
            if ap2 == 'PM':
                if int(hr2) != 12:
                    hr2 = int(hr2) + 12
            else:
                if int(hr2) == 12:
                    hr2 = 0

            templs = [hr1,min1,ap1,hr2,min2,ap2]
            printls = [s for s in templs if s != None and isinstance(s, int)]
            pstr = f'{printls[0]:02}:{printls[1]:02} to {printls[2]:02}:{printls[3]:02}'

            return pstr
        else:
            raise ValueError
    except ValueError:
        sys.exit('ValueError')

if __name__ == "__main__":
    main()