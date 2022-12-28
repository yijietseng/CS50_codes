import sys, csv


def main():
    check_argv(sys.argv)
    scourgify(sys.argv)

def scourgify(l):

    try:
        with open(l[1]) as f:
            reader = csv.DictReader(f)
            with open(l[2],'w') as o:
                writer = csv.DictWriter(o, fieldnames=['first','last','house'])
                writer.writeheader()
                for row in reader:

                    writer.writerow({'first': row['name'].split(',')[1].lstrip(' '),
                                     'last': row['name'].split(',')[0],
                                     'house': row['house']})
    except FileNotFoundError:
        sys.exit('Could not read invalid_file.csv')


def check_argv(l):
    # exit if too few argument
    if len(l) < 3 :
        sys.exit('Too few command-line arguments')
    # exit if too many argument
    elif len(l) > 3:
        sys.exit('Too many command-line arguments')
    # exit if no a CSV file
    elif '.csv' not in l[1]:
        sys.exit('Not a CSV file')

if __name__ == '__main__':
    main()
