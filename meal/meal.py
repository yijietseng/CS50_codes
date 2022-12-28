def main():
    timels = input('What time is it? ').strip().lower().split(' ')
    tf = convert(timels)
    if 7 <= tf <= 8:
        print('breakfast time')
    elif 12 <= tf <= 13:
        print('lunch time')
    elif 18 <= tf <= 19:
        print('dinner time')

def convert(t):
    time = t[0].split(':')

    # convert time from am or pm to 24-hr format
    if 'pm' in t or 'p.m.' in t:
        if time[0] == '12':
            hr = float(time[0])
        else:
            hr = float(time[0])+12
    elif 'am' in t or 'a.m.' in t:
        if time[0] == '12':
            hr = 0.0
        else:
            hr = float(time[0])
    # only account for the 24-hr format
    else:
        hr = float(time[0])

    mins = float(time[1])/60

    con = hr + mins
    return con

if __name__ == "__main__":
    main()