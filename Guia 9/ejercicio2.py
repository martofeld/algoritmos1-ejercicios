import random

# Ejercicio 2 A
def contar_palabras(cadena):
	"""Recibe una cadena y cuenta la cantidad de ocurrencias de palabras. Devuelve un diccionario con las palabras como clave y la cantidad como valor"""
	apariciones = {}
	for palabra in cadena.lower().split():
		apariciones[palabra] = apariciones.get(palabra, 0) + 1

	return apariciones

cadena = "Que lindo dia que hace hoy"
print(contar_palabras(cadena))

# Ejercicio 2 B
def contar_caracteres(cadena):
	"""Recibe una cadena y cuenta la cantidad de ocurrencias de caracteres. Devuelve un diccionario con las caracteres como clave y la cantidad como valor"""
	apariciones = {}
	for caracter in cadena.lower():
		apariciones[caracter] = apariciones.get(caracter, 0) + 1

	return apariciones

print(contar_caracteres(cadena))

# Ejercicio 2 C
def contar_dados(iteraciones):
	apariciones = {}
	for i in range(iteraciones):
		dado1 = random.randint(1,6)
		dado2 = random.randint(1,6)
		suma = dado1 + dado2
		apariciones[suma] = apariciones.get(suma, 0) + 1

	return apariciones

print(contar_dados(10))