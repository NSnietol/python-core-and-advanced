'''
Created on Nov 11, 2018

@author: nilson.nieto
'''
def custumgen(x,y):
    while x<y:
        yield x 
        x+=1


for i in custumgen(1, 4):
    print(i)
    
    
print(next(custumgen(7, 13)))