class Personaje():
	DIRECCION_X = 0
	DIRECCION_Y = 1

	def __init__(self, vida, posicion, velocidad):
		"""Vida: int, cantidad de vida. Posicion: tupla, posicion del personaje. Velocidad: int, velocidad con la que se mueve"""
		self.vida = vida
		self.posicion = posicion
		self.velocidad = velocidad

	def mover(self, direccion, cantidad):
		"""Direccion: int, DIRECCION_X o DIRECCION_Y"""
		self.posicion[direccion] += self.velocidad

	def recibir_ataque(self, dano):
		if self.vida < dano:
			raise ValueError("El personaje se quedo sin vida")

		self.vida -= dano

class Soldado(Personaje):

	def __init__(self, vida, posicion, velocidad, ataque):
		super(Soldado, self).__init__(vida, posicion, velocidad)
		self.ataque = ataque

	def atacar(self, personaje):
		personaje.recibir_ataque(self.ataque)

class Campesino(Personaje):

	def __init__(self, vida, posicion, velocidad, cosecha):
		super(Campesino, self).__init__(vida, posicion, velocidad)
		self.cosecha = cosecha

	def cosechar(self):
		return self.cosecha