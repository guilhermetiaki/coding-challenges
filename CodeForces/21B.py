eq1 = [int(i) for i in input().split(" ")]
eq2 = [int(i) for i in input().split(" ")]

a1, b1, c1 = eq1
a2, b2, c2 = eq2

if a1 == 0 and b1 == 0 and c1 != 0 or a2 == 0 and b2 == 0 and c2 != 0:
	print("0")
	exit()
elif a1*b2 == b1*a2 and b1*c2 == b2*c1 and a1*c2 == a2*c1:
	print("-1")
	exit()
elif a1*b2 == b1*a2:
	print("0")
	exit()
else:
	print("1")
	exit()