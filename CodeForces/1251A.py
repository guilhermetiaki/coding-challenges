t = int(input())

for i in range(t):
	string = list(input())

	string.append("0")

	working = set()

	i = 0
	while i < len(string):
		try:
			if string[i] == string[i+1]:
				i += 2
			else:
				working.add(string[i])
				i += 1
		except IndexError:
			i += 1

	working = list(working)
	working.sort()
	for w in working:
		print(w, end='')
	print()
