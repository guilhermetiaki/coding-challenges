while True:
	try:
		participants,budget,n_hotels,weeks = [int(i) for i in input().split(" ")]
	except:
		break

	hotels = []
	for i in range(0,n_hotels):
		hotels.append([])
		hotels[-1].append(int(input()))
		hotels[-1].append([int(i) for i in input().split(" ")])
		hotels[-1][-1].sort()

	hotels.sort(key=lambda x: x[0])

	for i in range(0,len(hotels)):
		cost = participants*hotels[i][0]
		if cost > budget:
			print("stay home")
			break
		if hotels[i][1][-1] >= participants:
			print(cost)
			break


