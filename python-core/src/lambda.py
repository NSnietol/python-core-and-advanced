'''
Created on Nov 11, 2018

@author: nilson.nieto
'''

f = lambda a,b,c=2: a*b*c

is_even = lambda a : a%2==0
sumar = lambda a=0, b=0: a+b

 
print(is_even(8))
print(f(1,3))

print(sumar(1,999))