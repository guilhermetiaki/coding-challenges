import math

def radians(angle):
	return angle*math.pi/180

def rotate_anticlockwise(x, y, pivotx, pivoty, angle):
	sin = math.sin(radians(angle))
	cos = math.cos(radians(angle))

	x = x - pivotx
	y = y - pivoty

	new_x = x*cos - y*sin
	new_y = x*sin + y*cos

	x = new_x + pivotx
	y = new_y + pivoty

	return x, y

def rotate_clockwise(x, y, pivotx, pivoty, angle):
	return rotate_anticlockwise(x, y, pivotx, pivoty, 360-angle)

def main():
	tests = int(input())
	for t in range(0,tests):
		commands = int(input())
		x = 0.0
		y = 0.0
		angle = 0.0
		for c in range(0,commands):
			command, argument = input().split(" ")
			if argument == "?":
				broken_command = command
				broken_angle = angle
				broken_x = x
				broken_y = y
			else:
				argument = int(argument)

				if command == "fd":
					tmp_x = x + argument
					x, y = rotate_anticlockwise(tmp_x, y, x, y, angle)
				elif command == "lt":
					angle += argument % 360
				elif command == "rt":
					angle -= argument % 360
				elif command == "bk":
					tmp_x = x + argument
					x, y = rotate_anticlockwise(tmp_x, y, x, y, angle-180)

		if broken_command == "fd":
			print(round(math.sqrt(x**2+y**2)))
		elif broken_command == "lt":
			i = 0
			new_x = x
			new_y = y
			attempt = 0
			while abs(new_x) > 0.01 or abs(new_y) > 0.01:
				attempt = i
				new_x, new_y = rotate_anticlockwise(x, y, broken_x, broken_y, i)
				i += 1
			print(attempt)
		elif broken_command == "rt":
			i = 0
			new_x = x
			new_y = y
			attempt = 0
			while abs(new_x) > 0.01 or abs(new_y) > 0.01:
				attempt = i
				new_x, new_y = rotate_clockwise(x, y, broken_x, broken_y, i)
				i += 1
			print(attempt)
		elif broken_command == "bk":
			print(round(math.sqrt(x**2+y**2)))

if __name__ == '__main__':
	main()