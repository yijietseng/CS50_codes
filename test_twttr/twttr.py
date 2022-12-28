def main():
    name = input("Input: ").strip()

    convert_name = shorten(name)

    print(convert_name)


def shorten(word):
    word = str(word)

    vowel = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

    for n in word:
        if n in vowel:
            word = word.replace(n, "")

    return word


if __name__ == "__main__":
    main()
