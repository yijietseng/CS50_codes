def main():
    fraction = cal_fraction()
    if fraction >= 99:
        print('F')
    elif fraction <= 1:
        print('E')
    else:
        print(str(fraction)+'%')

def cal_fraction():
    while True:
        try:
            x,y = input('Fraction: ').strip().rsplit('/')
            if int(x) > int(y):
                pass
            else:
                percent = round((int(x)/int(y))*100)
                return percent
        except (ValueError, ZeroDivisionError):
            pass

if __name__ == '__main__':
    main()