def wc(path):
	"""Dado un path de un archivo cuenta la cantidad de lineas, palabras y caracteres en el mismo e imprime el
	resultado por pantalla"""
	lineas = 0
	palabras = 0
	caracteres = 0
	with open(path) as f:
		for linea in f:
			linea = linea.strip()
			lineas += 1
			caracteres += len(linea)
			palabras += len(linea.split())

	print("Lineas:", lineas)
	print("Palabras:", palabras)
	print("Caracteres:", caracteres)

wc("archivo.txt")