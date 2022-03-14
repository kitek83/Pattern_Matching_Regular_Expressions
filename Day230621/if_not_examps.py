a = False
b = True
if not a:
    print('a is false')
else:
    print('a is true')
if not b:
    print('b is false')
else:
    print('b is true')

string_1 = ''
if not string_1:
    print('string_1 is empty')
else:
    print(string_1)
print('-------------------')

word = '123'
if not word.isdecimal():
    print('word has letters')
else:
    print('word has digits')
print('=========================')
ph_num = '415-555-4242'
print('len(ph_num: ',len(ph_num))
for x in range(1,13):
    print(x,end=',')