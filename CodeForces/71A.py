n = int(input())

for i in range(0,n):
	word = input()

	if len(word) <= 10:
		print(word)
	else:
		print (word[0] + str(len(word)-2) + word[-1])