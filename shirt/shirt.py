from PIL import Image as pic
from PIL import ImageOps as imops
import sys

def main():
    check_argv(sys.argv)
    overlay(sys.argv)

def overlay(l):
    try:
        shirt = pic.open('shirt.png')
        size = shirt.size
        doll = pic.open(l[1])
        doll = imops.fit(doll,size)
        doll.paste(shirt,shirt)
        doll.save(l[2])
    except FileNotFoundError:
        sys.exit('Input does not exist')


def check_argv(l):
    file_extension = ['jpg', 'jpeg', 'png']
    # exit if too few argument
    if len(l) < 3 :
        sys.exit('Too few command-line arguments')
    # exit if too many argument
    elif len(l) > 3:
        sys.exit('Too many command-line arguments')

    # check if arguments have correct extension
    elif l[1].split('.')[1] not in file_extension:
        sys.exit('Invalid input file')
    elif l[2].split('.')[1] not in file_extension:
        sys.exit('Invalid output file')
    # exit if output does not have the same extension as input
    elif l[1].split('.')[1] != l[2].split('.')[1]:
        sys.exit('Input and output have different extensions')


if __name__ == '__main__':
    main()
