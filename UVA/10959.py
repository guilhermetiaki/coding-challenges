import math
from collections import deque

def BFS(graph, source):
	queue = deque()
	visited = dict()
	distance = dict()
	for vertex in graph:
		visited[vertex] = False
		distance[vertex] = math.inf
	visited[source] = True
	distance[source] = 0
	queue.appendleft(source)

	while len(queue):
		u = queue.pop()
		for adjacent in graph[u]:
			if visited[adjacent] == False:
				visited[adjacent] = True
				distance[adjacent] = distance[u] + 1
				queue.appendleft(adjacent)

	return distance

cases = int(input())

for c in range(cases):
	input()

	persons, couples = map(int,input().split())

	graph = dict()
	for i in range(persons):
		graph[i] = []

	for i in range(couples):
		p1, p2 = map(int,input().split())

		graph[p1].append(p2)
		graph[p2].append(p1)

	distances = BFS(graph, 0)
	for i in range(1, persons):
		print(distances[i])
	if c != cases-1:
		print()