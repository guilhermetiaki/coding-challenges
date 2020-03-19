n = int(input())
while n != 0:
	n = [int(i) for i in str(n)]

	sum = 0
	for i in range(0,len(n)):
		sum = sum + n[i]
	n = [int(i) for i in str(sum)]

	while len(n) > 1:
		sum = 0
		for i in range(0,len(n)):
			sum = sum + n[i]
		n = [int(i) for i in str(sum)]
	print(sum)
	
	n = int(input())