fn = input('File name: ').lower().strip().rsplit('.')

image = ['gif','jpg','jpeg','png']
app = ['pdf','zip']
tp = ['txt']

# to check if it has file extansion
if len(fn) >= 2:
    if fn[-1] in image:
        if fn[-1] == 'jpg':
            print('image/jpeg')
        else:
            print('image/'+fn[-1])
    elif fn[-1] in app:
        print('application/'+fn[-1])
    elif fn[-1] in tp:
        print('text/plain')
    else:
        print('application/octet-stream')
# if no file extansion than execute
else:
    print('application/octet-stream')