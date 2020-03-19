while True:
	try:
		string = input()
	except Exception as e:
		exit()

	upper_even = 0
	lower_even = 0
	upper_odd = 0
	lower_odd = 0
	for x in range(0,len(string),2):
		if string[x] >= 'A' and string[x] <= 'Z':
			upper_even += 1
		else:
			lower_even += 1
	for x in range(1,len(string),2):
		if string[x] >= 'A' and string[x] <= 'Z':
			upper_odd += 1
		else:
			lower_odd += 1

	print(min(lower_even+upper_odd, upper_even+lower_odd))