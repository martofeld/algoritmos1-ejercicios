class Polinomio:
	"""docstring for Polinomio"""
	def __init__(self, coeficientes):
		self.coeficientes = coeficientes
	
	def __str__(self):
		reversed_c = list(reversed(self.coeficientes))
		to_str = ""
		for i in range(len(self.coeficientes) - 1, -1, -1):
			c = reversed_c[i]
			if i == 0:
				to_str += str(c)
				continue
			
			if i == 1:
				to_str += "x^{} + ".format(i)
			elif c != 0:
				to_str += "{}x^{} + ".format(c,i)

		return to_str

	def __eq__(self, other):
		if len(self.coeficientes) != len(other.coeficientes):
			return False

		for c in self.coeficientes:
			if not c in other.coeficientes:
				return False

		return True

	def derivar(self):
		l = len(self.coeficientes)
		d = []
		for c in self.coeficientes:
			l -= 1
			if l != 0:
				d.append(c * l)

		return Polinomio(d)

p1 = Polinomio([1,2,3,4])
print(p1)
p2 = Polinomio([4,3,2,1])
print(p2)

print(p1 == p2)

print(p1.derivar())
