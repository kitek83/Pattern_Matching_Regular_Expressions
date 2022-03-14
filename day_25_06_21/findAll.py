import re

phoneNumRegex = re.compile(r'\d\d\d\-\d\d\d-\d\d\d\d') #no groups
findNum = phoneNumRegex.findall('Phone nr to my work is 455-879-9988 and private phone is 477-789-9966')
print('found numbers are:',findNum)
print('Found numbers are:')
for num in findNum:
    print(num)