def main():
    y, m, d = format_output()
    print(y, m, d, sep='-')

def format_output():
    month = {
    "January":1,"February":2,"March":3,
    "April":4,"May":5,"June":6,
    "July":7,"August":8,"September":9,
    "October":10,"November":11,"December":12
    }

    while True:
        try:
            whole_date = input('Date: ').strip().title()
            # Check and get month output
            if '/' in whole_date:
                in_month, in_date, in_yr = whole_date.rsplit('/')
                if in_month.isdigit and 0 < int(in_month) <=12 :
                    out_month = f"{int(in_month):02d}"
                else:
                    raise ValueError
            elif ',' in whole_date:
                in_month, in_date, in_yr = whole_date.replace(',','').rsplit(' ')
                if in_month.isalpha() and in_month in month:
                    out_month = f"{int(month[in_month]):02d}"
            elif not ',' in whole_date or '/' not in whole_date:
                raise ValueError

            # Check if date is no more than 31 days
            if not 0 < int(in_date) <= 31:
                raise ValueError
            elif not int(in_yr) > 0:
                raise ValueError
            else:
                out_date = f"{int(in_date):02d}"
                out_yr = f"{int(in_yr):04d}"

            return [out_yr, out_month, out_date]

        except (ValueError,KeyError):
            pass

if __name__ == '__main__':
    main()