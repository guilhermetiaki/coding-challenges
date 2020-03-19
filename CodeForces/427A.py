n = int(input())
events = input().split()

free_oficers = 0
untreated_crimes = 0

for e in events:
	if e == "-1":
		if free_oficers > 0:
			free_oficers -= 1
		else:
			untreated_crimes += 1
	else:
		free_oficers += int(e)

print(untreated_crimes)