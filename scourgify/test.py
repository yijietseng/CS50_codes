import sys, csv


def main():
    #print(scourgify())
    scourgify()

def scourgify():

    try:
        name = []
        first = []
        last = []
        house = []
        with open('before.csv','r') as f:
            reader = csv.DictReader(f)
            with open('after.csv','w') as o:
                writer = csv.DictWriter(o, fieldnames=['first','last','house'])
                writer.writeheader()
                for row in reader:

                    writer.writerow({'first': row['name'].split(',')[1]})
                    writer.writerow({'last': row['name'].split(',')[0]})
                    writer.writerow({'house': row['house']})
                    '''
                    name.append(row['name'].split(','))
                    first.append(row['name'].split(',')[1])
                    last.append(row['name'].split(',')[0])
                    house.append(row['house'])
                    '''
            #return name

    except FileNotFoundError:
        sys.exit('Could not read invalid_file.csv')


if __name__ == '__main__':
    main()
