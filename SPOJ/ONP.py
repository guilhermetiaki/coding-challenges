t = int(input())

for x in range(0,t):
	exp = input()

	stack = []
	for x in range(0,len(exp)):
		if exp[x] >= 'a' and exp[x] <= 'z':
			print(exp[x],end='')
		elif exp[x] == ')':
			popped = stack.pop()
			while popped != '(':
				print(popped,end='')
				popped = stack.pop()

		else:
			stack.append(exp[x])

	print()

