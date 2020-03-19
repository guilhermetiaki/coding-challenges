from math import inf

t = int(input())

for i in range(t):
	n = int(input())
	array = list(map(int, input().split()))

	last_seen = dict()
	min_length = inf

	for j in range(len(array)):
		if array[j] in last_seen:
			length = j - last_seen[array[j]]
			min_length = min(min_length, length)
			last_seen[array[j]] = j
		else:
			last_seen[array[j]] = j

	if min_length != inf:
		print(min_length+1)
	else:
		print(-1)