q = int(input())

for x in range(0,q):
	coders, mathematicians, none = [int(i) for i in input().split(" ")]

	max_teams = min(coders, mathematicians, (coders+mathematicians+none)//3)

	print(max_teams)
