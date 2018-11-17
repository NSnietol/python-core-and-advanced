'''
Created on Nov 14, 2018

@author: nilson.nieto
'''


import re
string = 'Take up one idea. one idea at a time'

print(string)
print(re.search(r'o\w\w', string).group())

print(re.findall(r'o\w\w', string))

print(re.match(r't\w\w', 'take the risk or lost '))

string = 'Take 1 up One 23 idea. One idea 45 at a Time'
print(string)
print(re.findall(r'\d{1,2}',string ))
print(re.split(r'\d{1,2}',string ))

print('Replace')
print(string)

print(re.sub(r'One', 'two', string))


print('Find date')
string = 'Take 1 up One 23 idea. One idea 45 at a Time 20-11-2018'
print(string)

print(re.findall(r'\d{1,2}-\d{1,2}-\d{4}', string))


'''
\ CUALQUIER CARACTER DESPUES DE EL
. cualquier caracteres excepto un salto de linea
^ Inicio de cadena
$ Fin de cadena
[...] Rango

[^] Rango no valid
(...) opciones
(R | S ) OR

'''

