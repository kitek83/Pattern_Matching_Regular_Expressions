def check_if_phone(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
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


ph_num = '415-555-4242'
word1 = 'Moshi moshi'
print('Check if phone number ' + ph_num + 'is USA phone nr.')
print(check_if_phone(ph_num))
print('Chceck if' + word1 + 'is USA phone number')
print(check_if_phone(word1))
print()
print('-------------------')

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office'
for i in range(len(message)):
    chunk = message[i:i+12]
    if check_if_phone(chunk):  #if function returns value true
        print('USA pgone nr is: ',chunk)
print('Done')
