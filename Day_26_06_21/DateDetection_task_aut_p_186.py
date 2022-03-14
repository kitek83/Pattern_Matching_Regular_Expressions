import re

dateRegex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
text = '''I was born in 13/05/1983
        I finished studies in 22/10/3000
        I met Daniel in 12/04/2009'''
for groups in dateRegex.findall(text):
    #print(groups)
    print(3 * '-------------')
    date = '/'.join([groups[0],groups[1],groups[2]])
    print(date)

    if int(groups[0]) <= 31:
        if int(groups[1]) <= 12:
            if int(groups[2]) >=1000 and int(groups[2]) <= 2999:
                print('This is valid date.')
            else:
                print('Date is not valid.')
        else:
            print('Date is not valid.')
    else:
        print('Date is not valid.')