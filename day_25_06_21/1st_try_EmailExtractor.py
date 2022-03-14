import re
import pyperclip
text = pyperclip.paste()
emeilRegex = re.compile(r'\w+@\w+.pl')
emails = emeilRegex.findall(text)
print(emails)
print('Email list is: ')
count = 0
for email in emails:
    count += 1
    print(count,'.', email)


