# Ejercicio 3 A
class Corcho():
	def __init__(self, bodega):
		self.bodega = bodega

	def __str__(self):
		return "Bodega: {}".format(self.bodega)

# Ejercicio 3 B
class Botella():
	def __init__(self, corcho):
		self.corcho = corcho

	def __str__(self):
		return "Corcho: {}".format(self.corcho)

# Ejercicio 3 C
class Sacacorcho():
	def __init__(self):
		self.corcho = None

	def __str__(self):
		return "Corcho: {}".format(self.corcho)

	def destapar(self, botella):
		if not botella.corcho:
			raise ValueError("La botella ya esta destapada")

		if self.corcho:
			raise ValueError("El Sacacorcho ya tiene un corcho")

		self.corcho = botella.corcho
		botella.corcho = None

	# Ejercicio 3 D
	def limpiar(self):
		if not self.corcho:
			raise ValueError("El Sacacorcho no tiene ningun corcho para limpiar")

		self.corcho = None

corcho = Corcho("Nieto senetiner")
botella = Botella(corcho)
print("Botella", botella)

sacacorcho = Sacacorcho()
print("Sacacorcho", sacacorcho)

print("Destapando...", botella)
sacacorcho.destapar(botella)
print("Botella", botella)
print("Sacacorcho", sacacorcho)

print("Destapando otra vez...")
try:
	sacacorcho.destapar(botella)
except ValueError as e:
	print(e)

print("Destapando...", botella)
corcho2 = Corcho("Latitud 33")
botella2 = Botella(corcho2)
print("Destapando otra botella...")
try:
	sacacorcho.destapar(botella2)
except ValueError as e:
	print(e)

print("Limpiando sacacorcho...")
sacacorcho.limpiar()
print("Sacacorcho", sacacorcho)

print("Limpiando otra vez...")
try:
	sacacorcho.limpiar()
except ValueError as e:
	print(e)