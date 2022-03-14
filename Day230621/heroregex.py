import re
heroComp = re.compile(r'Batman|Tina Tarner')
mo1 = heroComp.search('Batman Tina Tarner')
print(mo1.group())

batRegex = re.compile(r'bat(man|mobile|bat|copter)')
mo2 = batRegex.search('Batman had batmobile with broken wheel.')
print(mo2.group())

batRegex2 = re.compile(r'Bat(wo)?man')
mo3 = batRegex2.search('The adventures of Batman.')
print(mo3.group())
mo4 = batRegex2.search('The adventures of Batwoman.')
print(mo4.group())