def is_phone(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return  False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True


print('Is it 488-788-9898 phone number?')
phone_nr = '488-788-9898'
print(is_phone(phone_nr))
print('Is it "masho mamashi" phone nr?')
phone_nr2 = 'masho mamashi'
print(is_phone(phone_nr2))

text_i = 'I haha the phone nr 554-333-1223. My work phone is 788-990-9999'
for i in range(len(text_i)):
    chunk = text_i[i:i+12]
    if is_phone(chunk):
        print('Phone nr is: ' + chunk)
    else:
        print('Not fitted chunks are: ' + chunk)



























