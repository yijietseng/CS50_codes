def main():
    m = int(input('m: '))
    Eng = cal(m)

    print('E:',Eng)

def cal(mass):
    c = 300000000
    E = mass*c**2

    return E

main()