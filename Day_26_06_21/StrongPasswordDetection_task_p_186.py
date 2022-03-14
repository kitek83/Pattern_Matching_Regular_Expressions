#In this 1st try 2n conditon is not fullfilled. Check next file .._2nd try, where conditions are fulfilled
import re
def passwCheck(pas):
    paswordRegex = re.compile(r'[a-zA-z0-9]')
    if len(pas) >= 8:
        print('Strong password '
              'but must contain both uppercase and lowercase.')
        if paswordRegex.findall(pas):
            print('Password is strong.')

    else:
        print('Password must contain at least 8 characters!')




password = input('Enter the password for checking if it is strong: ')
passwCheck(password)