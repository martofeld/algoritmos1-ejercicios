
def crear_agenda():
	agenda = {}
	while True:
		nombre = input("Ingrese un nombre o * para salir")

		if nombre == "*":
			break;

		if not nombre:
			print("Nombre invalido")
			continue

		if nombre in agenda:
			print("{}: {}".format(nombre, agenda[nombre]))
			control = input("Desea modificar el telefono? Si/No")
			if control.lower() == "si" or control.lower() == "s":
				modificar_telefono(agenda, nombre)
		else:
			modificar_telefono(agenda, nombre)

	return agenda

def modificar_telefono(agenda, nombre):
	while True:
		telefono = input("Que telefono desea para este contacto?")
		if telefono.isdigit():
			agenda[nombre] = telefono
			break
		else:
			print("El telefono debe contener solo numeros")


print(crear_agenda())