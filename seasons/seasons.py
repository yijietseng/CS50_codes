from datetime import date
import re, sys, inflect

def main():
    Bday = input('Date of Birth: ').strip()
    date_birth = get_Bday(Bday)
    date_today = date.today()
    delta = date_today - date_birth
    total_min = delta.days * 24 * 60
    p = inflect.engine()
    print(f'{p.number_to_words(total_min, andword = "").capitalize()} minutes')

def get_Bday(d):
    if re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', d):
        year, month, day = d.split('-')
        return date(int(year), int(month), int(day))
    else:
        sys.exit('Invalid date')




if __name__ == "__main__":
    main()