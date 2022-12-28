import sys
'''fsgdsf
'''

def main():
    print(get_len())

def get_len():
    # exit if too few argument
    if len(sys.argv) < 2 :
        sys.exit('Too few command-line arguments')
    # exit if too many argument
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    # exit if no a python file
    elif '.py' not in sys.argv[1]:
        sys.exit('Not a Python file')

    try:
        len_line = []
        with open(sys.argv[1]) as f:
            for line in f:
                line = line.replace('\n',' ')
                if line.isspace() == False:
                    line = line.lstrip(' ')
                    if line.startswith('#') == False:
                        len_line.append(line)

        return len(len_line)

    except FileNotFoundError:
        sys.exit('File does not exist')


if __name__ == '__main__':
    main()
