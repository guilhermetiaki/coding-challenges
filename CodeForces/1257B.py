t = int(input())

for i in range(t):
	x,y = map(int, input().split())

	if y <= x:
		print("YES")
		continue
	if x == 1:
		print("NO")
		continue
	if x == 2 and y != 3:
		print("NO")
		continue
	if x == 3:
		print("NO")
		continue

	if x%2 == 1:
		x_prime = 3*(x-1)/2
		if x_prime - x > 0:
			print("YES")
			continue
		else:
			print("NO")
			continue
	else:
		x_prime = 3*(x)/2
		if x_prime - x > 0:
			print("YES")
			continue
		else:
			print("NO")
			continue