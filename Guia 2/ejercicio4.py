def print_odd_numbers():
	start = int(input("Please input the first number"))
	end = int(input("Please input the second number"))
	start += start % 2
	for number in range(start, end + 1, 2)
		print(number)