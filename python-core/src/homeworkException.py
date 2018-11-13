'''
Created on Nov 12, 2018

@author: nilson.nieto
'''

class InvalidPasswordException(Exception):
    
    def __init__(self):
        print("Invalid password")



try:
    password = input('Ingrese el password')
    
    if(len(password)<6):
        raise InvalidPasswordException()
except InvalidPasswordException:
    print('Ingrese un password valido')        