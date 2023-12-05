### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Nel","Glez.", 26 } # Una vez le definimos elementos pasa de ser diccionario a set
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("NelGzz.")
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("NelGzz.") # Un set no admite elementos repetidos, al volver a añadir un elemento ya añadido anteriormente no lo incluye
print(my_other_set)
"""
my_other_set.pop("Nel") # TypeError: set.pop() takes no arguments (1 given)
print(my_other_set)
"""
print("Nel" in my_other_set ) # Al existir el elemento me saca un true
print("Nelw" in my_other_set )# Al no existir el elemento me saca un false

my_other_set.remove("Nel") # La función remove me elimina el elemento que le indiques del set
print(my_other_set)

my_other_set.clear() # La función clear elimina todos los elementos del set
print(my_other_set)

print(len(my_other_set))

del my_other_set 
# print(my_other_set) # La función "del" elimina el set definido, no es lo mismo que la función clear, que lo que hace es vaciar/eliminar los elementos del set   NameError: name 'my_other_set' is not defined

my_set = {"Nel","Glez.", 26 }
my_list = list(my_set)
print(my_list[0])

my_other_set = {"Kotlin","Swift.", "Python" }

my_new_set = my_set.union(my_other_set) # La función union sirve para unir, valga la redundancia, dos sets
print(my_new_set)

print(my_new_set.union({"JavaScript", "C++"}))

print(my_new_set.difference(my_set))
