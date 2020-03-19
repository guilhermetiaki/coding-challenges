t = int(input())

for test in range(t):
	rooms = int(input())
	stairs = input()

	first_stair = stairs.find("1")
	if first_stair == -1:
		first_stair = None

	last_stair = rooms - 1 - stairs[::-1].find("1")
	if last_stair == -1:
		last_stair == None

	if first_stair != None:
		starting_at_left = (last_stair+1)*2
		starting_at_right = (rooms - first_stair)*2
		print(max(starting_at_left, starting_at_right))
	else:
		print(rooms)
