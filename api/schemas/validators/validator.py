import re
regexEmail = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+([.]\w{2,})+$'


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

    

def validate_name(name):
    verify = True
    msgm = {}
    if len(name) < 3 or len(name) > 100:
        verify = False
        msgm['amount'] = 'Invalid amount.'
    if name[0] == ' ' or name[-1] == ' ':
        verify = False
        msgm['spaces'] = 'Invalid spaces.'
    for char in name:
        if char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúàèìòùâêîôûãõçÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÇ0123456789 ':
            verify = False
            msgm['char'] = 'Invalid character.'
    if verify == False:
        return msgm
    else:
        return True


def validate_text(text):
    verify = True
    msgm = {}
    if text == '':
        verify = False
        msgm['empty'] = 'Field must not be empty.'
    elif len(text) < 3 or len(text) > 100:
        verify = False
        msgm['amount'] = 'Invalid amount.'
    elif text[0] == ' ' or text[-1] == ' ':
        verify = False
        msgm['spaces'] = 'Invalid spaces.'
    for char in text:
        if char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúàèìòùâêîôûãõçÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÇ0 ':
            verify = False
            msgm['char'] = 'Invalid character.'
    if 'SELECT' in text or 'UPDATE' in text or 'DELETE' in text or 'INSERT' in text:
        verify = False
        msgm['bad_intention'] = 'Tentativa de injeção de SQL.'
    if verify == False:
        return msgm
    else:
        return True


def validate_description(description):
    msgm = {}
    verify = True
    if len(description) < 3:
        verify = False
        msgm['amount'] = 'Field must contain more than 3 characters.'
    if len(description) > 2048:
        verify  = False
        msgm['amount'] = 'Field must contain less than 2048 characters.'
    if description.find('select') != -1 or description.find('update') != -1 or description.find('delete') != -1 or description.find('insert') != -1:
        verify = False
        msgm['bad_intention'] = 'Sql injection attempt.'
    return True
