tests = int(input())
for i in range(tests):
	a,b,c = map(int,input().split())

	stones = 0

	fromBC = min(b,c//2)*3
	stones += fromBC
	b -= fromBC//3

	fromAB = min(a,b//2)*3
	stones += fromAB

	print(stones)