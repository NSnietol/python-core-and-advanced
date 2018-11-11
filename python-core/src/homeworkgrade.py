'''
Created on Nov 11, 2018

@author: nilson.nieto
'''



math = 35
physics = 80
chemestry = 78


if(math<35):
    print("Fail math  : ",math)
if(physics<35):
    print("Fail physics  : ",physics)
if(chemestry<35):
    print("Fail chemestry  : ",chemestry)

average = (math+physics+chemestry)/3

if(average<=59):
    print("Grade : C")
    
elif(average>59 and average<=69):
    print("Grade : B")
    
else:
    print("Grade : A")