import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My number is 788-988-9988')
print('Found number is: ',mo.group())

AttributeError: 'NoneType' object has no attribute 'group'