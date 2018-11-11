'''
Created on Nov 11, 2018

@author: nilson.nieto
'''

lst1=[1,2,3,4,5,6]


lst2=[1,65,2,5,64]

newList = [i for i in lst1 if i in lst2]


print(newList)