
def cargar_datos(archivo):
	"""recibe un nombre de archivo, cuyo contenido tiene el formato clave,valor y devuelva un diccionario con el
	primer campo como clave y el segundo como valor."""
	diccionario = {}
	with open(archivo) as a:
		for linea in a:
			clave,valor = linea.strip().split(",")
			diccionario[clave] = valor

	return diccionario

def guardar_datos(archivo, diccionario):
	with open(archivo, "w") as a:
		for clave,valor in diccionario.items():
			a.write("{},{}\n".format(clave, valor))

guardar_datos("ej7.csv", {1:"rojo", 2:"azul", 3:"amarillo", 4:"blanco"})

print(cargar_datos("ej7.csv"))