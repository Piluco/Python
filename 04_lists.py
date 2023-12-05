### Lists ###

my_list = list()
my_other_list = []


my_list = [35, 26, 61, 59, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [26, 1.81, "Nel", "Glez"]

print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[2])
print(my_other_list[3])
print(my_other_list[-1])
print(my_other_list[-2])
print(my_other_list[-3])
print(my_other_list[-4])
print(my_other_list.count("Nel"))
print(my_list.count(30))

my_other_list.append("NelGlez.")
print(my_other_list)

my_other_list.insert(1, "azul")
print(my_other_list)

my_other_list[1] = "negro"

my_other_list.remove("negro") 
print(my_other_list)

del my_list[2] # Del elimina por indice, sin saber el valor del elemento que se elimina, tampoco lo retorna como hace la función pop

my_list.remove(30) # Elimina por elemento, para ello tengo que conocer los elementos de la lista y agregarle el que yo desee a la función, elimina el primero elemento que le cuadre, en este caso le he dicho que elimine el 30 pero había dos 30 en la lista my_list, cuidado con esto
print(my_list)

print(my_list.pop()) # Quita el último elemento de la lista (por defecto), pero podemos hacer un print y vemos el elemento que hemos eliminado
print(my_list)

print(my_list.pop(2)) # lo mismo que la anterior pero seleccionando el elemento de la lista que queramos, retornandolo tmbn

my_pop_element = my_list.pop(1)
print(my_pop_element)


del my_list[2] # Elimina el elemento que le indico pero sin retornarlo 
print(my_list)

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]

print(age)

### Concatenación de listas ###

print(my_list + my_other_list)


my_other_other_list = [35, 15, 10, "Nel", "Glez"]

new_list = my_other_other_list.copy()

my_other_other_list.reverse() # ordenar los elementos de la lista ala reves ej. 4, 5, 5, 1 aplico reverse y se quedaría 1, 5, 5, 4

print(my_other_other_list)
print(new_list)