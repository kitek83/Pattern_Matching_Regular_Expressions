import re
regexWord =  re.compile(r'\d+\s\w+')
text = regexWord.findall('11 drums, 12 pipers, 10 lords, 8 maids, 7 swans')
print(text)