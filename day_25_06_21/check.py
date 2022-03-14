import re
noRegex = re.compile(r'[^aeiouAIEOU]')
find_text2 = noRegex.findall('Robocop eats baby food. BABY FOODS.')
print(find_text2)

list = ['cat','bat','cow','elephant']
string_joined = '-'.join(list)
print(string_joined)