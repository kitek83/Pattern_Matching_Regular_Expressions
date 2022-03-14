import re
import pyperclip
text = str(pyperclip.paste())   #copy the web page from tab contact from USA

phoneRegex = re.compile(r'''
(\+\d)?
(\s|-|\.)?
(\d{3})
(\.|s|-)
(\d{3})
(\.|\s|-)
(\d{4})
''',re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
\.[a-zA-z]{2,3}
)''',re.VERBOSE)
matches = []
for groups in phoneRegex.findall(text):
    phone_nr= '-'.join([groups[0],groups[2],groups[4],groups[6]])
    print(phone_nr)
    #print(groups[6])
    matches.append(phone_nr)

for groups in emailRegex.findall(text):
    print(groups)
    matches.append(groups)
print()
print('=====================')

if  len(matches) > 0:
    pyperclip.copy(''.join(str(matches)))

