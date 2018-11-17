'''
Created on Nov 14, 2018

@author: nilson.nieto
'''

from datetime import *
print('Combine time + date')


t =time(8,30)
d = date(2018,2,20)


df = datetime.combine(d,t)


print(df)
