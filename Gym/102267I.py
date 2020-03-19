n = int(raw_input())

string = raw_input()

i = 0;

list = []

while i < len(string):
	if string[i] <= '9' and string[i] >= '0':
		begin = i
		i = i + 1
		while i < len(string) and string[i] <= '9' and string[i] >= '0':
			i = i + 1
		i = i - 1
		list.append(int(string[begin:i+1]))
	else:
		list.append(string[i])

	i=i+1

stack = []

supervisor = [None] * (n+1)

stack.append(list[0])

supervisor[stack[0]] = 0

for x in xrange(1,len(list)):
	if list[x] == '(':
		stack.append(list[x+1])
	elif list[x] == ')':
		stack.pop()
	else:
		try:
			supervisor[list[x]] = stack[-2]
		except:
			pass

for x in xrange(1,len(supervisor)):
	print str(supervisor[x]),