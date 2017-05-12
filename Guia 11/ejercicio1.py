class Fraccion():
	# Ejercicio 1 A
	def __init__(self, dividendo, divisor):
		self.dividendo = dividendo
		self.divisor = divisor

	def __str__(self):
		return "{}/{}".format(self.dividendo, self.divisor)	

	# Ejercicio 1 B
	def sumar(self, other):
		divisor = self.divisor * other.divisor
		dividendo1 = (self.dividendo * divisor) // self.divisor
		dividendo2 = (other.dividendo * divisor) // other.divisor
		dividendo = dividendo1 + dividendo2

		return Fraccion(dividendo, divisor)

	# Ejercicio 1 C
	def multiplicar(self, other):
		divisor = self.divisor * other.divisor
		dividendo = self.dividendo * other.dividendo
		return Fraccion(dividendo, divisor)

	def simplificar(self):
		mcm = self._obtener_mcm()
		self.divisor = self.divisor // mcm
		self.dividendo = self.dividendo // mcm

	def _obtener_mcm(self):
		"""Utiliza el argoritmo de euclides para calcular el multiplo comun mayor"""
		if self.divisor == self.dividendo:
			return self.divisor

		mayor = self.divisor
		menor = self.dividendo

		if mayor < menor:
			mayor,menor = menor,mayor

		while True:
			resto = mayor % menor
			if resto == 0:
				return menor
			
			mayor = menor
			menor = resto

fraccion = Fraccion(1, 2)
print(fraccion)

print(fraccion.sumar(Fraccion(1, 2)))

print(fraccion.multiplicar(Fraccion(2, 3)))

f = Fraccion(4,12)
f.simplificar()
print(f)