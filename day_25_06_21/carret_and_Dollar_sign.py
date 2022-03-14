import re
regex1 = re.compile(r'^Hello')
print(regex1.search('Hello World'))
find = regex1.search('He said hello.')
print(find)
print(find == None)

regex2 = re.compile(r'\d$')
print(regex2.search('Your age is 42'))
print(regex2.search('You are intelligent') == None)

regex3= re.compile(r'.at')
find = regex3.findall('The cat in the hat sat on the flat mat.')
print(find)
print('------------------')
regex4 = re.compile(r'First name: (.*) Last name: (.*)')
find = regex4.search('First name: Kris Last name: Kozak ')
print(find.groups())
print(find.group(1))
print(find.group(2))

nonGreedyRegex = re.compile(r'<.*?>')
find2 = nonGreedyRegex.search('<To serve man> for dinner.')
print(find2.group())
greedyRegex = re.compile(r'<.*>')
find3 = greedyRegex.search('<To serve man> for dinner.')
print(find3.group())

newlineRegex = re.compile(r'.*')
print(newlineRegex.search('Serve the public trust.\n Protect the innocent\n Uphold the low.').group())
print()

newlineRegex2 = re.compile(r'.*', re.DOTALL)
print(newlineRegex2.search('Serve the public trust.\nProtect the innocent\nUphold the low.').group())
print('====================')
ignoreCase = re.compile(r'Robocop', re.I)
print(ignoreCase.search('Robocop is part man, part machine.').group())
print(ignoreCase.search('ROBOCOP protecets the innocents.').group())
print(ignoreCase.search('You are talking too much about robocop.').group())

























