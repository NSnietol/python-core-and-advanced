'''
Created on Oct 28, 2018

@author: nilson.nieto
'''
lst = ['NS',12,-4,0.5]

print(lst)
lst.append(12)

print(lst)
print("Reverse")
print(lst[::-1])
print("Length")
print(len(lst))
lst.remove(12)
print("remove by value = 12",lst)

del(lst[0])
print("remove by index (0)",lst)

print("Max value",max(lst))

print("Min value",min(lst))