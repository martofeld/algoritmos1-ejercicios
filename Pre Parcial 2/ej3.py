class Colectivo:
	"""docstring for Colectivo"""
	def __init__(self):
		self.personas = {}
		
	def subir(self, destino, persona):
		personas = self.personas.get(destino, [])
		personas.append(persona)
		self.personas[destino] = personas

	def bajar(self, destino):
		if destino in self.personas:
			return self.personas.pop(destino)

		return []

	def __str__(self):
		return str(self.personas)


class Persona:
	"""docstring for Persona"""

	def __init__(self, n):
		self.nombre = n

	def __str__(self):
		return self.nombre

c = Colectivo()

c.subir("a", Persona("martin"))
print(c)
c.subir("a", Persona("paz"))
print(c)
c.subir("b", Persona("eric"))
print(c)
c.subir("c", Persona("sol"))
print(c)
c.bajar("d")
print(c)
c.bajar("a")
print(c)