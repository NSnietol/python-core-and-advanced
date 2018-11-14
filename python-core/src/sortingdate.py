'''
Created on Nov 14, 2018

@author: nilson.nieto
'''
from datetime import *
import time 

initTime = time.perf_counter()

listdates=[]


d1 = date(2016,8,12)

d2 = date(2017,4,12)

d3 = date(2018,7,12)

d4 = date(2005,8,12)

listdates.append(d1)
listdates.append(d2)
listdates.append(d3)
listdates.append(d4)


listdates.sort()

time.sleep(3)
print(listdates)

print('Execution time : ',time.perf_counter()-initTime)