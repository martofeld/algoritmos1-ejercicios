
def parse():
	with open("input_ej4.csv") as i, open("errors_ej4.txt", "a") as e_file:
		i.readline() #Titles

		out = {}
		for line in i:
			try:
				ano, mes, vendedor, cliente, monto = line.strip().split(",")
				s = out.get(vendedor, 0)
				print(s)
				out[vendedor] = s + int(monto)
			except Exception as e:
				print(e)
				e_file.write("Invalid line " + line + "\n")

	return out

print(parse())