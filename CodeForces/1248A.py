t = int(input())

for i in range(t):
	n_lines_1 = int(input())
	lines_1 = list(map(int, input().split()))
	n_lines_2 = int(input())
	lines_2 = list(map(int, input().split()))

	even_1 = 0
	for l in lines_1:
		if l%2 == 0:
			even_1 += 1
	odd_1 = n_lines_1 - even_1

	even_2 = 0
	for l in lines_2:
		if l%2 == 0:
			even_2 += 1
	odd_2 = n_lines_2 - even_2

	print(even_1*even_2 + odd_1*odd_2)