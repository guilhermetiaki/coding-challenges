long_name = input()

for i in range(0, len(long_name)):
	if i == 0 or long_name[i-1] == '-':
		print(long_name[i], end = '')
print()
