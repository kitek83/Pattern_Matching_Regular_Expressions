import re
findPhoone = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
text = 'My number is 999-888-7894'
mo = findPhoone.search(text)
print('You found: ', mo.groups())
country_code,phone_number = mo.groups()
print('country code: '+ country_code,'\nphone number: ' + phone_number)