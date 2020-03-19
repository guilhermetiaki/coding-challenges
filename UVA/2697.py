import math

n = int(input())

for i in range(n):
	number = int(input())
	if 0 <= number <= 1:
		print("1")
		continue
	else:
		digits = 0
		for i in range(2, number+1):
			digits += math.log10(i)
		digits = math.floor(digits) + 1
		print(digits)