import re
import pyperclip

text = str(pyperclip.paste())
phoneRegex = re.compile(r'(\+\d\d\s)(\d\d\s)(\d\d\d\s\d\d\s\d\d)')
emailRegex = re.compile(r'\w+@+\w+.pl')
matches = []
for groups in phoneRegex.findall(text):
    #print(groups)
    phoneNr ='-'.join([groups[0],groups[1],groups[2]])
    print(phoneNr)
    matches.append(phoneNr)
print(matches)
for groups in emailRegex.findall(text):
    print(groups)
    matches.append(groups)
print(matches)
for match in matches:
    print(match)
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))


