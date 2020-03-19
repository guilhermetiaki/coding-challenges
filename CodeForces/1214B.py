b = int(input())
g = int(input())
n = int(input())

decks = n+1

if(b < n):
	decks -= n-b

if(g < n):
	decks -= n-g

print(decks)