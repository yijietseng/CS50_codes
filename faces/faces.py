def main():
    words = input()
    new_words = convert(words)
    print(new_words)
def convert(words):
    words = words.strip().title()
    wordsls = words.split()
    face_dic = {':)':'🙂', ':(':'🙁'}
    replaced_word = ''
    for i in wordsls:
        if i in face_dic.keys():
            i = face_dic[i]
            replaced_word += i+' '
        else:
            replaced_word += i+' '
    return replaced_word


main()