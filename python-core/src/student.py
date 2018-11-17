'''
Created on Nov 13, 2018

@author: nilson.nieto
'''
import pickle




class Student:
    
    def __init__(self,idStudent,name,testcore):
        
        self.__id=idStudent
        self.__name=name
        self.__testcore=testcore
        
    def display(self):
        print(self.__id,self.__name,self.__testcore)
        
    def save(self):
        file = open('data-info.dat','wb')
        pickle.dump(self,file)
        file.close()



s = Student('12','Nilson',12321)

s.save()



