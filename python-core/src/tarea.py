'''
Created on Nov 3, 2018

@author: nilson.nieto

primeFlag =True

number = int(input("Number : "))

for i in range(2,number):
    if( number%i==0):
        primeFlag=False
        
if(primeFlag==True):
    print("Is Prime")
else:
    print("Not is prime")
'''    
number = int(input("Number : "))
i = number
while (i<100):
    i+=1
    if(i%10==0):
        continue
    print(i)
    
