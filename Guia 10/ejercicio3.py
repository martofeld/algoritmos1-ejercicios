def cut(path, delimitador, campos):
	"""Recibe un path de un archivo, un delimitador y una lista de campos. Muestra unicamente los campos pasados 
	con los valores del archivo separados por el delmimitador. La primera linea del archivo deben ser los nombres de los 
	campos. Los campos y valores deberan estar separados por una coma"""
	with open(path) as file:
		campos_archivo = file.readline().strip().split(",")
		index_campos = []
		for campo in campos:
			index = campos_archivo.index(campo)
			if index > -1:
				index_campos.append(index)

		for linea in file:
			row = linea.strip().split(",")
			to_print = []
			for i in index_campos:
				to_print.append(row[i])
			print(delimitador.join(to_print))

cut("input_ej3.csv", " # ", ["nombre", "apellido", "padron"])