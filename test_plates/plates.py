def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # if there is a space or punctuation, then return false
    for l in s:
        if not l.isalpha() and not l.isdigit():
            return False
    #check first two characters
    if s[:2].isalpha():
        # check length
        leng = len(s)
        if 2 <= leng <= 6:
            # check if there are any digits
            rest_s = s[2:]
            dig_ls = []
            for i in rest_s:
                dig_ls.append(i.isdigit())

            # if there are digits then check if the first digit is 0
            if any(dig_ls):
                check0 = []
                for k in rest_s:
                    if k.isdigit():
                        check0.append(k)
                if check0[0] == '0':
                    return False
                # If the first number is not 0, then check ending numbers
                else:
                    # loop through trues till it hits false
                    n = len(dig_ls)-1
                    while n >= 0:
                        if dig_ls[n]:
                            n -= 1
                        # once hit a false, loop through to find the next true
                        else:
                            while n >= 0:
                                n -= 1
                                if dig_ls[n] and n >= 0:
                                    return False
                                    break
                                elif not dig_ls[n] and n >= 0:
                                    return True
                                    break

            # if it's all character then check if there are any spaces or punctuations
            else:
                return True

            return True
        else:
            return False
    else:
        return False



if __name__ == '__main__':
    main()