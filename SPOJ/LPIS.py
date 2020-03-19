length = int(input())

sequence = [int(i) for i in input().split()]

max_sequence = max(sequence)

lpis_ending_in = [0] * (max_sequence + 1)

lpis = [0] * length

for i in range(0, length):
	lpis[i] = lpis_ending_in[sequence[i] -1] + 1
	lpis_ending_in[sequence[i]] = lpis[i]

print(max(lpis))
