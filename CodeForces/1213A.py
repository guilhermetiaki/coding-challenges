n = int(raw_input())

coordinates = [int(x) for x in raw_input().split(" ")]

parity = [x%2 for x in coordinates]

# print parity

evens = 0
odds = 0
for x in xrange(0,len(parity)):
	if parity[x] == 0:
		evens = evens + 1
	else:
		odds = odds + 1

if evens > odds:
	print odds
else:
	print evens