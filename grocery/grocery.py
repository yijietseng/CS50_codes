def main():
    d = {}
    itemls = ['APPLE',
            'BANANA',
            'LETTUCE',
            'MANGO',
            'MILK',
            'ORANGE',
            'PINEAPPLE',
            'STRAWBERRY',
            'SUGAR',
            'SWEET POTATO',
            'TORTILLA'
    ]
    while True:
        try:
            item = input().strip().upper()
            if item not in d and item in itemls:
                d[item] = 1
            elif item not in d and item not in itemls:
                raise KeyError
            elif item in d:
                d[item] += 1
        except EOFError:
            print()
            # sort dictionary
            sorted_keys = sorted(d.keys())
            sorted_d = {key:d[key] for key in sorted_keys}

            # print out dictionary
            for i in sorted_d:
                print(sorted_d[i], i)
            break
        except KeyError:
            pass
main()