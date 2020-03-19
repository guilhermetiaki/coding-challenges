n,m = [int(x) for x in input().split(" ")]

s = input()

t = input()

if "*" in s:
	s = s.split("*")
	if (s[0] == t[0:len(s[0])] or len(s[0])  == 0) and (s[1] == t[-len(s[1]):]  or len(s[1]) == 0)and len(s[0]) + len(s[1]) <= len(t):
		print("YES")
	else:
		print("NO")
else:
	if s == t:
		print("YES")
	else:
		print("NO")