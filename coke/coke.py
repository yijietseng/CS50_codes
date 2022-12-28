def main():
    due = 50
    print('Amount Due:',due)

    cal(due)

def cal(d):
    accept = [25, 10, 5]
    while 0 < d <= 50:
        insert = int(input('Insert Coin: '))
        if insert in accept:
            d -= insert
        if d > 0:
            print('Amount Due:',d)
        elif d <= 0:
            d = abs(d)
            print('Change owed:',d)
            break

if __name__ == '__main__':
    main()
