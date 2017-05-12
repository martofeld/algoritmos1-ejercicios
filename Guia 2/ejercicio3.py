import "./ejercicio2"

def show_conversion_table():
	print("|---------------------|")
	print("| farenhait | celcius |")
	for f in range(0, 120, 10):
		celcius = ejercicio2.farenhait_to_celcius(f)
		print("|", f, "|", celcius)
	print("|---------------------|")