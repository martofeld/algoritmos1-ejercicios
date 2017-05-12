def calcular_comision(ventas, comision):
	if not validar_vendedores(ventas.keys(), comision.keys()):
		raise ValueError("Los diccionarios no contienen a los mismos vendedores")


	with open("output_ej5.csv", "w") as out:
		for vendedor in ventas:
			out.write(vendedor+ ":"+str(ventas[vendedor] * comision[vendedor]) + "\n")
		

def validar_vendedores(lista1, lista2):
	if len(lista1) != len(lista2):
		return False

	for vendedor in lista1:
		if not vendedor in lista2:
			return False
	return True

calcular_comision({"a": 5, "b": 8, "c": 1}, {"a": 4, "c":2, "b":9})

try:
	calcular_comision({"a": 5, "b": 8, "c": 1}, {"a": 4, "c":2})
except Exception as e:
	print(e)