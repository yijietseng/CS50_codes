def main():
    mathexp = input('Expression: ').strip().split(' ')
    print(cal(mathexp))

def cal(t):
    if t[1] == '+':
        value = float(float(t[0]) + float(t[2]))
        return f"{value:.1f}"
    elif t[1] == '-':
        value = float(float(t[0]) - float(t[2]))
        return f"{value:.1f}"
    elif t[1] == '*':
        value = float(float(t[0]) * float(t[2]))
        return f"{value:.1f}"
    elif t[1] == '/':
        if t[2] != 0:
            value = float(float(t[0]) / float(t[2]))
            return f"{value:.1f}"
        else:
            return 'Not defined'


main()