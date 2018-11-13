'''
Created on Nov 12, 2018

@author: nilson.nieto
'''

class Patient:    
    def getId(self):
        return self.__idPatient
    def getName(self):
        return self.__name
    
    def getSsn(self):
        return self.__ssn
    
    def setId(self,idPatient):
        self.__id=idPatient
    def setSsn(self,ssn):
        self.__ssn=ssn
        
    def setName(self,name):
        self.__name = name
        
        
p = Patient()
p.setId(123)
print(p.id)
        