import "math"

def calculate_rectangle_perimeter(base, height):
	return 2 * (base + height)

def calculate_rectangle_area(base, height):
	return base * height

def calculate_rectangle_in_plane(x1, y1, x2, y2):
	return abs(x2 - x1) * abs(y2 - y1)

def calculate_circle_perimeter(radio):
	return 2 * radio * math.PI

def calculate_circle_area(radio):
	return math.PI * (radio ** 2)

def calculate_sphera_area(radio):
	return (4 / 3) * math.PI * (radio ** 3)

def calculate_rectangle_triangle_hipotenuse(catet1, catet2):
	return math.sqrt(catet1 ** 2 + catet2 ** 2)