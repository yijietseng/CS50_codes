
def main():
    name = input('Input: ').strip()

    convert_name = convert(name)

    print(convert_name)

def convert(t):
    vowel = ['a','A','e','E','i','I','o','O','u','U']

    for n in t:
        if n in vowel:
            t = t.replace(n,'')

    return t

if __name__ == '__main__':
    main()
