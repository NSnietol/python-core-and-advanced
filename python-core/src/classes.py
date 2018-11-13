'''
Created on Nov 11, 2018

@author: nilson.nieto
'''


class Product:
    
    def __init__(self):
        self.name="Iphone x10"
        self.description="Phone by Apple"
        self.price = 3500
    def __init__(self,name,description,price):
        self.name=name
        self.description=description
        self.price = price
    
    
product1 = Product("Mac Book","Laptop by Apple",3004)
    
print(product1.name)
    
    
    