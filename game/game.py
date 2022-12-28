import random


def main():
    rand_n = get_n()
    guess_n(rand_n)


def get_n():
    # Get level
    while True:
        try:
            level = int(input('Level: ').strip())
            if level <= 0:
                raise ValueError
        except ValueError:
            pass
        else:
            return random.randint(1,level)

def guess_n(n):
    while True:
        try:
            guess = int(input('Guess: ').strip())
            if guess > n:
                print('Too large!')
            elif guess < n:
                print('Too small!')
            else:
                print('Just right!')
                break
        except ValueError:
            pass

if __name__ == '__main__':
    main()