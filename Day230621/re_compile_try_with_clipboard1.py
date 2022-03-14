import pyperclip
import re
try:
    findPhone = re.compile(r'\d\d\s\d\d\s\d\d\s\d\d\s\d\d\d')
    text = pyperclip.paste()

    mo = findPhone.search(text)
    print('Searched number is:', mo.group())
    print()
except AttributeError:
    print('The number was not found.')
#print(text)