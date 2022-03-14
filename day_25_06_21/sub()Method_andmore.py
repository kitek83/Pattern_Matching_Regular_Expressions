import re
subRegex = re.compile(r'Agent \w+')
print(subRegex.findall('Agent Alice gave the correct documents to Agent Bob.'))

subRegex2 = re.compile(r'Agent \w+')
sub = subRegex2.sub('ROBOCOP','Agent Alice gave the correct documents to Agent Bob.')
print(sub)
print('-----------------')
subRegex3 = re.compile(r'Agent (\w)\w*')
sub = subRegex3.sub(r'1***', 'Agent Alice told Agent Carol, that Agent Eve knew Agent Bob was a double agent.')
print(sub)
