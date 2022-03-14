import re
import pyperclip
try:
    text = str(pyperclip.paste())
    regexPhone = re.compile(r'\+\d\d\s\d\d\s\d\d\d\s\d\d\s\d\d')
    mo = regexPhone.findall(text)
    print('Found numbers are: ',mo)
    print('Found numebrs are:')
    count = 0
    for num in mo:
        count += 1
        print(count,'. ',num)
except:
    print('Number was not found.')
