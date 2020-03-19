if __name__ == '__main__':
	presents, boxes = map(int, input().split())

	not_all_boxes_empty = 2**boxes - 1

	all_combinations = pow(not_all_boxes_empty, presents, 10**9+7)

	print(all_combinations)