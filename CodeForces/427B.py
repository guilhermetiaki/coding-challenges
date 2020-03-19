all_prisioners, crime_limit, transfer_prisioners = map(int, input().split())

crime_level = list(map(int, input().split()))

total_ways = 0
size = 0

for i in range(all_prisioners):
	if crime_level[i] <= crime_limit:
		size += 1
	else:
		if size >= transfer_prisioners:
			total_ways += size - transfer_prisioners + 1
		size = 0

	i += 1

if size >= transfer_prisioners:
	total_ways += size - transfer_prisioners + 1
print(total_ways)

