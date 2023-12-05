VARIABLES

my_string_variable = "my string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
(print(my_string_variable, my_int_to_str_variable, my_bool_variable))
print("Este es el valor de:", my_bool_variable)

# Alguna funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea, ¡OJOOOO! CUIDADO CON ABUSAR DE ESTA SINTAXIS, puede ser un foco de errores si cambio de posición "Manuel" por "González" puestol que hace mas complicado el posterior mantenimiento del código
name, surname, alias, age= "Manuel", "González", "Piluco", 26
print("Me llamo", name, surname, ", mi edad es", age,"y mi alias es", alias)

# Inputs
"""
name = input("¿Cuál es tu nombre? ")
age = input("¿Cuántos años tienes? ")
print(name)
print(age)
"""

# Cambiamos su tipo  COMO SE PUEDE OBSERVAR SI LANZAMOS EL CÓDIGO, INICIALMENTE DEFINÍ LA VARIABLE NAME COMO UNA CADENA DE TEXTO AHORA LA HE CAMBIADO A UN NÚMERO, SI VARAIS PERSONAS TRABAJAMOS SOBRE EL MISMO CÓDIGO Y ALGUIEN LE ASIGNA A NAME EL VALOR DE AGE PODRÍAMOS ACABAR TENIENDO UN PROBLEMÓN
name = 26
age = "Manuel"
print(name)
print(age)


# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.5
print(type(address))




