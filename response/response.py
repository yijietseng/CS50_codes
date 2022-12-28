from validator_collection import validators, errors, checkers

def main():
    print(validate(input('What is your email: ').strip()))

def validate(s):
    try:
        email = validators.email(s)
        if checkers.is_email(email):
            return 'Valid'
        else:
            return 'Invalid'
    except (errors.EmptyValueError, ValueError, errors.InvalidEmailError):
        return 'Invalid'
        

if __name__ == '__main__':
    main()