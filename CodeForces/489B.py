boys = int(input())

boys_skill = [int(i) for i in input().split(" ")]
boys_skill.sort()

girls = int(input())

girls_skill = [int(i) for i in input().split(" ")]
girls_skill.sort()

pairs = 0
i = 0
j = 0
while i < boys and j < girls:
	diff = boys_skill[i] - girls_skill[j]
	if abs(diff) <= 1:
		pairs += 1
		i += 1
		j += 1
	elif diff < 0:
		i += 1
	else:
		j += 1

print(pairs)