kirito_strength, n_dragons = map(int, input().split())

dragons = []
for i in range(n_dragons):
	tmp_strength, tmp_bonus = map(int, input().split())
	dragons.append([])
	dragons[-1].append(tmp_strength)
	dragons[-1].append(tmp_bonus)

# print(dragons)

# Sort dragons by strength
dragons.sort(key=lambda x: x[0])

# print(dragons)

for i in range(n_dragons):
	if kirito_strength > dragons[i][0]:
		kirito_strength += dragons[i][1]
	else:
		print("NO\n")
		exit()

print("YES\n")