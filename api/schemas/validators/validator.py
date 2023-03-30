import re
regexEmail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
regexName = '/\b[A-Za-zÀ-ú][A-Za-zÀ-ú]+,?\s[A-Za-zÀ-ú][A-Za-zÀ-ú]{2,19}\b/gi'


def email_validate(email):
    if(re.search(regexEmail,email)):  
        return True  
    else:  
        return False
    

def pass_validate(password):
    while not (re.search(r'.{8,}', password) and   
           re.search(r'[A-Z]', password) and 
           re.search(r'\d', password) and   
           re.search(r'[!@#$%¨&*]', password)):
        return False