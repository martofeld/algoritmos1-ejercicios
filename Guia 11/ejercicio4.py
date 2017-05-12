class Mate():

	def __init__(self, cantidad_cebadas):
		self.cebadas_restantes = cantidad_cebadas
		self.vacio = True

	def cebar(self):
		if not self.vacio:
			raise ValueError("Cuidado! Te quemaste!")

		self.vacio = False

	def beber(self):
		if self.vacio:
			raise ValueError("El mate esta vacio!")

		if self.cebadas_restantes:
			self.cebadas_restantes -= 1
		else:
			print("Advertencia: el mate esa lavado")

		self.vacio = True

cebadas_mate = 2
mate = Mate(cebadas_mate)
try:
	print("Tomando mate...")
	mate.beber()
except ValueError as e:
	print(e)
for i in range(cebadas_mate + 2): # Dos mates lavados
	print("Cebando mate...")
	mate.cebar()
	print("Tomando mate...")
	mate.beber()

print("Cebando mate...")
mate.cebar() # Cebo de nuevo
try:
	print("Cebando mate...")
	mate.cebar() # Ups ya esta lleno
except ValueError as e:
	print(e)
