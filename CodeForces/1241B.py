query = int(input())

for q in range(query):
	s = list(input())
	t = list(input())

	set_s = set(s)
	set_t = set(t)
	if len(set_s & set_t) == 0:
		print("NO")
		continue
	else:
		print("YES")
		continue
