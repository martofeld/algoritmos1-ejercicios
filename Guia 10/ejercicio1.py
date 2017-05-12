def head(path, lineas):
	"""Recibe el path de un archivo y la cantidad de lineas a leer del mismo y las imprime en pantalla"""
	with open(path) as f:
		for i in range(lineas):
			print(f.readline().strip())

head("archivo.txt", 15)