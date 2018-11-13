'''
Created on Nov 12, 2018

@author: nilson.nieto
'''


try:
    
    a = 23/0
except Exception:
    print("Error")
    
else:
    print("When doesnt exist error")
finally:
    print("Always")
