import itertools

n = input()

l = list( ''.join(i) for i in itertools.product("47", repeat=len(n)))

print(l.index(n) + 2**(len(n))-1)