'''
Created on Nov 11, 2018

@author: nilson.nieto
'''
def decorator(fun):
    def inner(n):
        return fun(n)+" How are you?"
    return inner
@decorator
def hello(name):
    return "Hello "+name


print(hello('Nilson'))