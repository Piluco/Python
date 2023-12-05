### Dictionaries ###   

my_dict = dict()
my_other_dict = {}


print(type(my_dict))
print(type(my_other_dict))


my_other_dict = {"Nombre": "Nel", "Apellido": "Glez.", "Edad": 26, 1:"Python"} # Muy importante los ":" sin ellos, el dict pasaría a ser set, podemos mezclar "string" y "int" sin ningún problema
print(my_other_dict)
print(len(my_other_dict)) # Los elementos se definen de par en par (relación clave valor) la estructura del dict sirve para relacionar datos

my_dict = {
    "Nombre": "Nel",
    "Apellido": "Glez.",
    "Edad": 26, 
    "Lenguajes": {"Python","Swift","Kotlin"}, # Un diccionario que como calve tiene un string pero como valor tiene un set dentro
    1: 1.83,
    "Asistentes": ["Piluco","Chachiña","DeviceK","Dhenison"] # Un diccionario que como calve tiene un string pero como valor tiene una lista dentro
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"]) # Para acceder al elemento en concreto, entre [] ponemos su clave

my_dict["Nombre"] = "Manuel" # Para cambiar el valor a la clave
print(my_dict["Nombre"])
print(my_dict)

print(my_dict[1])

my_dict["calle"] = "Calle Gijón" # Para agregar una nueva clave con su respectivo valor
print(my_dict)

del my_dict["calle"] # Para eliminar un elemento en concreto de nuestro dict, ¡¡¡¡OJO cuidado que si no definimos el elemento a eliminar nos eliminaría el dic como tal!!!! NameError: name 'my_dict' is not defined
print(my_dict)

print("Nel" in my_dict)
print("Nombre" in my_dict)
#print("Nelw" in my_dict)

print(my_dict["Nombre"]) 

print(my_dict.items())  # listado de cada uno de los items(claves y valores)
print(my_dict.keys())  # listado de solo claves
print(my_dict.values())  # listado de solo valores

my_new_dict = my_other_dict.fromkeys(("Nombre", 1, "Piso")) # .fromkeys es para crear un diccionario con las claves que definamos pero sin añadir valores a las mismas
print(my_new_dict)

