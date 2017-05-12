def cadena_mas_larga_por_caracter(cadena):
	"""Busca la palabra mas larga que contenga a cada caracter en la cadena dada"""
	cadena = cadena.lower()
	palabras = {}

	for caracter in cadena:
		for palabra in cadena.split():
			if caracter in palabra:
				largo_guardado = len(palabras.get(caracter, ""))
				if largo_guardado < len(palabra):
					palabras[caracter] = palabra

	return palabras

cadena = "que es eso eso es queso"
print(cadena, ":", cadena_mas_larga_por_caracter(cadena))

cadena = "Hola manola"
print(cadena, ":", cadena_mas_larga_por_caracter(cadena))