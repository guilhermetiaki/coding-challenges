t = int(raw_input())

for x in xrange(0,t):
	a,b = [int(y) for y in raw_input().split()]

	mod = []
	mod.append(a%10)
	i = 1
	while True:
		mod.append((mod[i-1]*mod[i-1])%10)
		if 2**i >= b:
			break
		i = i+1

	b_bin = [int(i) for i in str(bin(b))[2:]]
	b_bin = b_bin[::-1]

	out = 1
	for y in xrange(0, len(b_bin)):
		if b_bin[y] != 0:
			out = mod[y]*out
		# print out
	print out%10