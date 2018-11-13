'''
Created on Nov 12, 2018

@author: nilson.nieto
'''
from abc import abstractmethod,ABC
class TouchScreenLaptop(ABC):
    
    @abstractmethod
    def scroll(self):
        pass
    
    @abstractmethod
    def click(self):
        pass

class Hp(TouchScreenLaptop,ABC):
    
    
    @abstractmethod
    def click(self):
        pass
        
    
    def scroll(self):
        print("Scroll hp")

class Dell(TouchScreenLaptop,ABC):
    
    def scroll(self):
        print("Scroll dell")
        
    @abstractmethod
    def click(self):
        pass
    
class HPNotebook(Hp):
    
    def click(self):
        print("Click hp")

class DELLNotebook(Dell):
    
    def click(self):
        print("Click dell")
        
        
hp = HPNotebook()

hp.click()
dell = DELLNotebook()
dell.click()