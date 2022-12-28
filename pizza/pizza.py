import sys, csv
from tabulate import tabulate


def main():
    print(get_manu())

def get_manu():
    # exit if too few argument
    if len(sys.argv) < 2 :
        sys.exit('Too few command-line arguments')
    # exit if too many argument
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    # exit if no a python file
    elif '.csv' not in sys.argv[1]:
        sys.exit('Not a CSV file')

    try:
        manu = []
        with open(sys.argv[1]) as f:
            reader = csv.reader(f)
            for row in reader:
                manu.append(row)
        return tabulate(manu[1:], manu[0], tablefmt="grid")

    except FileNotFoundError:
        sys.exit('File does not exist')


if __name__ == '__main__':
    main()
