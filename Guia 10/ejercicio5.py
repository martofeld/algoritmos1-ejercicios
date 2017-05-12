def grep(path, expresion):
	"""Dado el path de un archivo y una expresion imprime unicamente las lineas del archivo que contienen a la mismas"""
	with open(path) as f:
		for linea in f:
			if expresion in linea:
				print(linea.strip())


print("grep", "1")
grep("archivo.txt", "1")
print("grep", "2")
grep("archivo.txt", "2")
print("grep", "3")
grep("archivo.txt", "3")
print("grep", "ine")
grep("archivo.txt", "ine")