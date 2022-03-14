import re
#checking if there is in the password at least  one uppercase character
def uppercase(password):
    if re.search('[A-Z]',password):
        return True
    return False
#checking if there is in the password at least  one lowercase character
def lowercase(password):
    if re.search('[a-z]',password):
        return True
    return False
#checking if there is in the password at least  one digit
def digit(password):
    if re.search('[0-9]',password):
        return True
    return False

def user_input_password_check():
    password = input('Enter the password for checking: ')
    if len(password) >= 8 and uppercase(password) and lowercase(password) and digit(password):
        print('Password is strong.')
    else:
        print('Password is weak.')

user_input_password_check()