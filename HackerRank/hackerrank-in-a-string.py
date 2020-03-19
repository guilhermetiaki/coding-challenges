q = int(raw_input())

match = "hackerrank"

for x in range(0,q):
	string = raw_input()

	i = 0
	for c in string:
		if i < len(match) and match[i] == c:
			i += 1

	if i == len(match):
		print "YES"
	else:
		print "NO"
