N = int(raw_input())

total = 0

for x in xrange(0,N+1):
	rectangles = N/(x+1) - x
	if rectangles > 0:
		total = total + rectangles
	else:
		break

print total