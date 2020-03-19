from math import ceil

t = int(input())

for i in range(t):
	lectures, classes, lectures_per_pen, classes_per_pencil, pencilcase_max = map(int,input().split())

	pens = ceil(lectures/lectures_per_pen)
	pencils = ceil(classes/classes_per_pencil)

	if pens+pencils <= pencilcase_max:
		print(pens, pencils)
	else:
		print(-1)