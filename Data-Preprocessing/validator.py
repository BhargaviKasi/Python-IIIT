import re
def phoneNumValidator(number):
    p='[6-9][0-9]{9}$|^[0][6-9][0-9]{9}|^[+][9][1][6-9][0-9]{9}$'
    if re.match(p,number):
        return True
    else:
        return False        

def MailValidator(id):
    p='[a-z][0-9a-z]{7,25}[@][a-z]{3,8}.[a-z]{2,4}|[a-z][0-9a-z.]{7,25}[@][0-9a-z]{8}.[a-z]{2,6}.[a-z]{2,3}'
    if re.match(p,id):
        return True
    else:
        return False