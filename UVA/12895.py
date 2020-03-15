T = int(input())

for i in range(0, T):
	N = input()

	n = len(N)

	sum = 0
	for c in N:
		sum = sum + int(c)**n
		
	if sum == int(N):
		print("Armstrong")
	else:
		print("Not Armstrong")