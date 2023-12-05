# Strings

my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea" # \n = a salto de linea
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación" # Básicamente deja un margen(tabula) al inicio de la frase
print(my_tab_string)

my_scape_string = "\tEste es un String \n escapado" # Básicamente deja un margen(tabula) al inicio de la frase y un salto e linea sin el margen
print(my_scape_string)

# Formateo strings

name, surname, age = "Manuel", "González", 26

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # Para tirar datos
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # Para formatear datos
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))  #Forma cutre de tirar datos no recomendada
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Para formatear datos + rapido que la otra manera

# Desempaquetado de caracteres

language = "Python"
a, b, c, d, e, f, = "Python"
print(a)
print(e)

# División 

language_slice = language [1:3]
print(language_slice)

language_slice = language [1:]
print(language_slice)

language_slice = language [-2] # -2 = 2º caracter empezando por el final
print(language_slice)

language_slice = language [1:]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del sistema

print(language.capitalize()) # Pasar la primera máyuscula
print(language.upper()) # Pasar todo a mayúsculas
print(language.count("t")) # Cuenta el nº de caracteres iguales
print(language.isnumeric())
print(language.lower()) # Pasar todo a minúsculas
print(language.upper().isupper())
print(language.startswith("Py"))