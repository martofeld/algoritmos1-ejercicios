class Vector():

	# Ejercicio 2 A
	def __init__(self, elementos):
		self.elementos = elementos

	def __str__(self):
		str_elementos = [str(i) for i in self.elementos]
		return "[ {} ]".format(", ".join(str_elementos))

	#Ejercicio 2 B
	def escalar(self, escalar):
		return Vector([x * escalar for x in self.elementos])

	#Ejercicio 2 C
	def sumar(self, other):
		if len(self.elementos) != len(other.elementos):
			raise ValueError("Los vectores tienen distintos tamaños, no se pueden sumar")

		return Vector([self.elementos[i] + other.elementos[i] for i in range(len(self.elementos))])




vector = Vector([1,2,3,4])
print(vector)

print(vector.escalar(4))

print(vector.sumar(Vector([4,3,2,1])))