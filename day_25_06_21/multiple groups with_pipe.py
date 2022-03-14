import re

regex = re.compile(r'Batman|Tina Fay')
mo = regex.search('Batman and Tina Fay are main heroes')
print(mo.group())

regex2 = re.compile(r'Bat(man|mobile|copter|bat)')
mo2 = regex2.search('Batmobile lost the wheel and Batcopter flies very fastly.')
print(mo2.group())
print(mo2.group(1))

regex3 = re.compile(r'Bat(wo)?man')
mo3 = regex3.search('The main heroe was the Batman')
print('---------------')
print(mo3.group())
mo4 = regex3.search('The main heroe was Batwoman')
print(mo4.group())
print()
regex4 = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
mo5 = regex4.search('My number is 589-789-8877')
print('Phone nr: ' + mo5.group())
mo6 = regex4.search('My number is 784-9988')
print('Nr withour country code:' + mo6.group())
print('================')

try:
    regex5 = re.compile(r'Bat(wo)*man')
    mo7 = regex5.search('I like Batwoman')
    print(mo7.group())
    mo8 = regex5.search('Thi is very strange Batwowowowoman')
    print(mo8.group())
except:
    print('Latters are case sensitive.')
print('##################')
regex6 = re.compile(r'Bat(wo)+man')
mo9 = regex6.search('The best heroe is Batwoman')
print(mo9.group())
#mo10 = regex6.search('Lastly I watched Batman.')
#print(mo10.group())
greedyRegex = re.compile(r'(Ha){3,5}')
mo10 = greedyRegex.search('He was laughing HaHaHaHaHa')
print(mo10.group())
nongreedyRegex = re.compile(r'(Ha){3,5}?')
mo11 = nongreedyRegex.search('He was laughing HaHaHaHaHa')
print(mo11.group())






















