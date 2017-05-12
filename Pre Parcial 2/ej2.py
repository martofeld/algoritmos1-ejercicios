n1 = int(input("Ingrese un numero"))
n2 = int(input("Ingrese otro numero"))

with open("input_ej2.csv") as i:
	with open("output_ej2.csv", "w") as o:
		line = i.readline().strip().split(",")
		line[n1], line[n2] = line[n2], line[n1]
		o.write(",".join(line))