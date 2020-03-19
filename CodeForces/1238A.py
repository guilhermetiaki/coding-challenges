t = int(input())

for i in range(t):
	x,y = map(int, input().split())

	diff = x-y

	# check if diff is multiple of a prime

	if diff != 1:
		print("YES")
	else:
		print("NO")
