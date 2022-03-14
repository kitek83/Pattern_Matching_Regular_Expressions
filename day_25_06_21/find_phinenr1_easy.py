import pyperclip
import re

text = pyperclip.paste()
phoneNr = re.compile(r'(\+\d\d)\s(\d\d)\s(\d\d\d\s\d\d\s\d\d)')
mo = phoneNr.search(text)
print('Nr found is:' + mo.group())
print('Country code is:' + mo.group(1))
print('City code is:' + mo.group(2))
print('Rest Phone nr:' + mo.group(3))