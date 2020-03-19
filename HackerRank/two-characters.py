from itertools import combinations 

trash = int(input())

string = input()

all_chars = list(set(string))

comb = list(combinations(all_chars, 2) )

max = 0

for c in comb:
	filtered = list(filter(lambda x: (x in c), string))
	
	valid = True

	char_1 = filtered[0]
	for x in range(0,len(filtered),2):
		if filtered[x] != char_1:
			valid = False

	char_2 = filtered[1]
	for x in range(1,len(filtered),2):
		if filtered[x] != char_2:
			valid = False

	if char_1 != char_2 and valid:
		# print(c, filtered)
		if len(filtered) > max:
			max = len(filtered)
print(max)