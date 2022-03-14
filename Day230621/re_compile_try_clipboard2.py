import re
import pyperclip
try:
    findPhone = re.compile(r'(\+\d\d)\s(\d\d)\s(\d\d\d\s\d\d\s\d\d)')
    text = pyperclip.paste()
    mo = findPhone.search(text)
    print('Found number(s) are/is: ',mo.groups())
    print('Country code:'+mo.group(1))
    print('City code:' + mo.group(2))
    print('Phone number:' + mo.group(3))
except AttributeError:
    print('Phone number was not found.')