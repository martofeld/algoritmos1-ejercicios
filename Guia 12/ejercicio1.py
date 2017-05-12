class Papel():
	def __init__(self):
		self.texto = ""

	def __str__(self):
		return self.texto

	def escribir(self, cadena):
		self.texto += cadena

class Birome():
	def __init__(self, tinta):
		self.tinta = tinta

	def escribir(self, texto, papel):
		if self.tinta < len(texto):
			raise ValueError("La lapicera no tiene mas tinta")

		self.tinta -= len(texto)
		papel.escribir(texto)

	def __str__(self):
		return "Tinta restante: {}".format(self.tinta)

class Marcador(Birome):
	"""docstring for Marcador"""
	def __init__(self, tinta):
		super(Marcador, self).__init__(tinta)

	def recargar(self, tinta):
		self.tinta += tinta


papel = Papel()

print("Nuevo marcador :)")
marcador = Marcador(5)
print(marcador)
print("Escribiendo...")
marcador.escribir("Hola", papel)
print(marcador)
print("Recargando...")
marcador.recargar(4)
print(marcador)
print("Resultado:", papel)

print("Nuevo marcador :)")
lapicera = Birome(6)
print("Escribiendo...")
try:
	lapicera.escribir("Hola mundo!", papel)
except ValueError as e:
	print(e)
lapicera.escribir("Hola m", papel)
print("Resultado:", papel)