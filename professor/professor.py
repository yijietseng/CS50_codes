import random


def main():
    l,h = get_level()
    score = 0
    for _ in range(10):
        try:
            x, y = generate_integer(l,h)
            result = x + y
            ans = int(input(str(x)+' + '+str(y)+' = ').strip())
            if ans == result:
                score += 1
            else:
                wrong_attemp = 0
                while True:
                    wrong_attemp += 1
                    print('EEE')
                    ans = int(input(str(x)+' + '+str(y)+' = ').strip())
                    if ans == result:
                        score += 1
                        break
                    elif wrong_attemp >= 2:
                        print(str(x)+' + '+str(y)+' = '+str(result))
                        break

        except ValueError:
            print('EEE')
            pass

    print('Score:',score)


def get_level():
    while True:
        try:
            level = int(input('Level: ').strip())
            if level <= 0 or level >= 4:
                raise ValueError
        except ValueError:
            pass
        else:
            # return a minimum number and a maximum number with n digits
            return 10**(level-1), (10**level)-1

def generate_integer(low, level):
    if low < 10:
        x = random.randint(0, level)
        y = random.randint(0, level)
    else:
        x = random.randint(low, level)
        y = random.randint(low, level)
    return x, y

if __name__ == "__main__":
    main()