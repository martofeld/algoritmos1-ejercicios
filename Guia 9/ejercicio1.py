def tuplas_a_diccionario(tuplas):
	"""Convierte una lista de tuplas a un diccionario usando el primer elemento de la tupla como clave y el segundo como valor"""

	diccionario = {}
	for clave,valor in tuplas:
		valores = diccionario.get(clave, [])
		valores.append(valor)
		diccionario[clave] = valores

	return diccionario

l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días') ]
print(tuplas_a_diccionario(l))