'''
Created on Nov 13, 2018
@author: nilson.nieto
'''
import pickle

f = open('data-info.dat','rb')

obj = pickle.load(f)

obj.display()