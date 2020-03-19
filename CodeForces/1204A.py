import sys

s = int(raw_input(), 2)

# print s

trains = 0
time = 1
while True:
	if s <= time:
		break
	else:
		time = time * 4
		trains = trains + 1

print trains
