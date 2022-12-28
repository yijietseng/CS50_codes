def main():
    camel = input('camelCase: ').strip()
    snake = convert2snake(camel)
    print(snake)

def convert2snake(t):
    s = ''
    for i in range(len(t)):
        if t[i].islower():
            s += t[i]
        elif t[i].isupper():
            s += '_'+t[i].lower()
    s = s.lstrip('_')

    return 'snake_case: '+s

if __name__ == '__main__':
    main()