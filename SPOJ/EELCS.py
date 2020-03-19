def common_subsequence(string_a, string_b, index_a, index_b):
	if index_a == 0 or index_b == 0:
		return 0
	elif string_a[index_a-1] == string_b[index_b-1]:
		return 1 + common_subsequence(string_a,string_b,index_a-1,index_b-1)
	else:
		return max(common_subsequence(string_a,string_b,index_a-1,index_b),common_subsequence(string_a,string_b,index_a,index_b-1))

string_a = input()
string_b = input()

print(common_subsequence(string_a,string_b,len(string_a),len(string_b)))