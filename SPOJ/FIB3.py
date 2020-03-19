T = int(raw_input())

fib = []
fib.append(0)
fib.append(1)
for x in range(2,61):
	fib.append(fib[x-1] + fib[x-2])

for x in range(0,T):
	n = int(raw_input())

	index = fib.index(n)

	if index<6:
		print "impossible"
	else:
		print str(fib[index-4]) + " " + str(fib[index-3]) + " " + str(fib[index-1])
