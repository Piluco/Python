### Tuplas ### conjunto de valores, a diferencia de las listas que se definen con [] , la tupla se define con () y son inmutables, en tuplas no puedo cabiar elementos como tal

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (26, 1.81, "Nel", "Glez.", "NelGlez." )
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[3])
#  print(my_tuple[-4]) # pete xD no hay valor -6 IndexError  #

print(my_tuple.count("Glez.")) # Cuenta cuantos "Glez." hay en la tupla en este caso
print(my_tuple.index("Nel")) # Cuenta en que posición esta el elemento de la tupla, en este caso "Nel" está en la posición 2, ¡¡¡¡OJO QUE LA PRIMERA POSICIÓN ES 0 SIEMPRE!!!!
"""
my_tuple[1] = 1.83   # Las tuplas son inmutables por lo que me va a dar error si cambio el elemento 1 de 1.81 a 1.83  """"""'tuple' object does not support item assignment""""""
print(my_tuple)
"""

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)   # Nueva tupla, conjunto de las dos tuplas creadas anteriormente

print(my_sum_tuple[3:6]) # Me saca entre el indice 3 y el 6 sin contar el 6 esto es un slice 

my_tuple = list(my_tuple) # con esto cambiamos el tipo, por lo que transformaríamos mu tupla en una lista, que si que es mutable
print(type(my_tuple))

my_tuple[4] = "NelGzz." 
my_tuple.insert(1, "negro") # Añadimos datos nuevos por que al ser una lista es mutable
my_tuple = tuple(my_tuple) # Lo volvemos a convertir en tupla 
print(my_tuple) 
print(type(my_tuple)) 

del my_tuple #
#print(my_tuple) NameError: name 'my_tuple' is not defined