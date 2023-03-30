import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def email_validate(email):
    if(re.search(regex,email)):  
        return True  
    else:  
        return False
    

def pass_validate(password):
    while not (re.search(r'.{8,}', password) and   
           re.search(r'[A-Z]', password) and 
           re.search(r'\d', password) and   
           re.search(r'[!@#$%¨&*]', password)):
        return False