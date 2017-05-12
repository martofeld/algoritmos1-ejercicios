def calculate_triangular_numbers(n):
	triangular = 0
	for i in range(1, n + 1):
		triangular += i
		print(i, "-", triangular)

def calculate_triangular_numbers_with_formula(n):
	for i in range(1, n + 1):
		triangular = n * (n + 1)/2
		print(i, "-", triangular)