from math import sqrt

def perfectSquare(n):
	root = sqrt(n)
	if int(root + 0.5) ** 2 == n:
		return True, int(root + 0.5)
	else:
		return False, -1

def primes(n):
	prime = [True] * (n+1)
	p = 2
	while (p * p <= n):
		if (prime[p] == True):
			for i in range(p * p, n+1, p):
				prime[i] = False
		p += 1

	return prime

def TPrime(n):
	if n == 4:
		return True
	if n < 9:
		return False
	if n%2 == 0:
		return False
	ps, root = perfectSquare(n)
	if not ps:
		return False
	if prime[root] == False:
		return False

	return True

def main():
	t = int(input())

	tests = map(int, input().split())

	for t in tests:
		if TPrime(t):
			print("YES")
		else:
			print("NO")


if __name__ == '__main__':
	prime = primes(10**6)
	main()