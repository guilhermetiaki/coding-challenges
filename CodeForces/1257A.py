q = int(input())

for i in range(q):
	row_size, max_swaps, a_position, b_position = map(int, input().split())

	push_to_right = max(a_position, b_position)
	push_to_left = min(a_position, b_position)

	# push as much as possible to the right
	if row_size - push_to_right > max_swaps:
		a_position = push_to_right + max_swaps
		max_swaps = 0
	# push to the extreme right
	else:
		a_position = row_size
		max_swaps -= row_size - push_to_right

	# push as much as possible to the left
	if push_to_left > max_swaps:
		b_position = push_to_left - max_swaps
	# push to the extreme left
	else:
		b_position = 1

	print(a_position - b_position)
