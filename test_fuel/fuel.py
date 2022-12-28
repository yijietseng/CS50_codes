def main():
    fraction = convert(input('Fraction: ').strip())
    print(gauge(fraction))

def convert(fraction):
    while True:
        try:
            x,y = fraction.rsplit('/')
            x = int(x)
            y = int(y)
            percent = x/y
            if percent < 1:
                percent = round((int(x)/int(y))*100)
                return percent
            else:
                fraction = input('Fraction: ').strip()
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
