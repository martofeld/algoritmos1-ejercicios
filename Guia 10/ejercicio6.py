LOW_A = 97
LOW_Z = 122
CAP_A = 65
CAP_Z = 90

def rot13(input_file, output_file):
	"""Recibe un archivo, los cifra y lo guarda en el output"""
	with open(input_file) as inp, open(output_file, "w") as out:
		for linea in inp:
			out.write(cifrar_linea(linea))


def cifrar_linea(linea):
	linea_cifrada = ""
	for char in linea:
		ascii_code = ord(char)
		if(ascii_code >= LOW_A and ascii_code <= LOW_Z or ascii_code >= CAP_A and ascii_code <= CAP_Z):
			linea_cifrada += cifrar_caracter(ascii_code)
		else:
			linea_cifrada += char
	return linea_cifrada

def cifrar_caracter(char):
	return chr((char + 13) % 26)

rot13("archivo.txt", "output_ej6.txt")