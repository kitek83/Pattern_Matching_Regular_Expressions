import re
import pyperclip
text = str(pyperclip.paste())

phoneRegex = re.compile(r'''
(\+\d\d)?
(\s\-\.)


''',re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-z]{2,3})
)''',re.VERBOSE)

for groups in phoneRegex.findall(text):
    phone_nr= '-'.join(groups[0],groups[1])
    print(phone_nr)