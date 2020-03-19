lenght = int(input())
string1 = input()
string2 = input()

flip = [False] * lenght

cost = 0

for i in range(0, lenght):
	if string1[i] != string2[i]:
		flip[i] = True
		cost += 1

for i in range(0,lenght-1):
	if flip[i] and flip[i+1] and string1[i] != string1[i+1]:
		flip[i] = False
		flip[i+1] = False
		cost -= 1

print(cost)