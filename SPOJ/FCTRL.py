T = int(raw_input())

for x in xrange(0,T):
	N = int(raw_input())
	power = 5
	zeros = 0
	while True:
		if N >= power:
			zeros = zeros + N/power
			power = power*5
		else:
			break
	print zeros