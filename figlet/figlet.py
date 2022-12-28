from pyfiglet import Figlet
from sys import argv
import sys, random

def main():

    if len(argv) >= 2:
        if '-f' in argv or '--font' in argv:
            out = convert2ASCII(f=argv[2])
            print('Output:',out)
        else:
            sys.exit('Invalid usage')
    else:
        out = convert2ASCII()
        print('Output:',out)

def convert2ASCII(f=False):

    fig = Figlet()
    if bool(f):
        if f in fig.getFonts():
            text = input('Input: ').strip()
            fig.setFont(font=f)
        else:
            sys.exit('Invalid usage')
    else:
        text = input('Input: ').strip()
        f = random.choice(fig.getFonts())
        fig.setFont(font=f)

    return fig.renderText(text)


if __name__ == '__main__':
    main()

