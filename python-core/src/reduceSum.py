from functools import  reduce



lst = [1,2,3,4,5,6,7]

print(reduce(lambda x,y : x+y, lst))
