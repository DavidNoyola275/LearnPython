# Variables
my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable) #Un numero lo acabamos conviertiendo a una cadena de texto con el str()
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

print("----------------------------------------------------------")
# Concatenacion de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de: ", my_bool_variable)

print("----------------------------------------------------------")
# Algunas funciones del sistema
print(len(my_string_variable)) #len() nos devuelve la longitud de la cadena de texto

print("----------------------------------------------------------")
# Variables en una sola linea. ¡Esto es una mala practica!, pero si se puede hacer.
name, surname, alias, age = "David", "Noyola", "Noyolita", 20
print("Me llamo: ", name, surname, ". Mi edad es: ", age, ". Y mi alias es:", alias)

print("----------------------------------------------------------")
"""
# Inputs
first_name = input("Cual es tu nombre: ")
age = input("Cual es tu edad: ")

print("Tu nombre es: ", first_name)
print("Tu edad es: ", age)
"""

print("----------------------------------------------------------")
#Cambiamos su tipo
name = 20
age = "Noyolita"
print(name)
print(age)

print("----------------------------------------------------------")
# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))