import inflect


def main():
    allNames = get_names()
    print(adieu_out(allNames))


def get_names():
    names = []
    while True:
        try:
            name = input("Name: ").strip().title()
            names.append(name)
        except EOFError:
            print()
            break
    return names


def adieu_out(l):
    p = inflect.engine()
    out = "Adieu, adieu, to " + p.join(l)
    return out


if __name__ == "__main__":
    main()
