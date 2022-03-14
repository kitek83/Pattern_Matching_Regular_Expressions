import re
ownRegex = re.compile(r'[aeiouAEIOU]')
find_text = ownRegex.findall('Robocop eats baby food. BABY FOODS.')
print(find_text)

noRegex = re.compile(r'[^aeiouAIEOU]')
find_text2 = noRegex.findall('Robocop eats baby food. BABY FOODS.')
print(find_text2)