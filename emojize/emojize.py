import emoji as em


def main():
    text = input("Input:").strip()
    print("Output:", em.emojize(text))


if __name__ == "__main__":
    main()
