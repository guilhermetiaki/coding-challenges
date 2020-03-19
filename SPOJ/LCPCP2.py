T = int(raw_input())

for x in xrange(0,T):
	line = raw_input().split(" ")
	b = int(line[0])
	e = int(line[1])
	m = int(line[2])

	mod = []
	mod.append(b%m)
	i = 1
	while True:
		mod.append((mod[i-1]*mod[i-1])%m)
		if 2**i >= e:
			break
		i = i+1

	e_bin = [int(i) for i in str(bin(e))[2:]]
	e_bin = e_bin[::-1]

	out = 1
	for y in xrange(0, len(e_bin)):
		if e_bin[y] != 0:
			out = mod[y]*out
	print str(x+1) + ". " + str(out%m)