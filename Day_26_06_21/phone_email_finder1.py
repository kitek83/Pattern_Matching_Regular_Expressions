import re
import pyperclip

#phone finder part
text = pyperclip.paste()
phoneRegex1 = re.compile(r'''
(\+\d{2})?
(\s|-|\.)?
(\d{2})
(\s|-|\.)
(\d{3})
(\s|-|\.)
(\d{2})
(\s|-|\.)
(\d{2})
''', re.VERBOSE)

emailRegex = re.compile(r'''
[a-zA-Z0-9_.%-]+
@
[a-zA-Z0-9_.]+
[a-zA-Z]''',re.VERBOSE)

emailRegex2 = re.compile(r'\w+@\w+\.pl') #This method is good only for matched web pages

matches = []
for groups in phoneRegex1.findall(text):
    #print(groups)
    phoneNr = '-'.join([groups[0],groups[2],groups[4],groups[6],groups[8]])
    print(phoneNr)
    matches.append(phoneNr)
print(3*'############')
print()
print('No I will use the simple regex\+\d{2}?\s?\d{2}\s\d{3}\s\d{2}\s\d{3}')

phoneRegex2 = re.compile(r'(\+\d{2}\s)?(\d{2}\s)(\d{3}\s\d{2}\s\d{2})')
for groups1 in phoneRegex2.findall(text):
    #print(groups1)
    phoneNr2 = '-'.join([groups1[0],groups1[1],groups1[2]])
    print(phoneNr2)
#finding email etendd method
for groups in emailRegex.findall(text):
    print(groups)
    matches.append(groups)

print()
print('Finding emails due to short method')
print(2*'===========================')
for groups in emailRegex2.findall(text):
    print(groups)























