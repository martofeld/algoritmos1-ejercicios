MAX_BYTES_TO_READ = 100

def cp(input_path, output_path):
	"""Recibe un path de entrada y uno de salida y copia el input al archivo de output"""
	with open(input_path, "rb") as inp, open(output_path, "wb") as out:
		read = inp.read(MAX_BYTES_TO_READ)
		while read:
			out.write(read)
			read = inp.read(MAX_BYTES_TO_READ)

cp("archivo.txt", "output_ej2.txt")
cp("imagen.jpg", "output_imagen_ej2.jpg")