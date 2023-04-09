import random

def bucket_sort(li, n=100, max_num=10000):
	step = max_num//n
	bucket = [[] for _ in range(n)]
	for each in li:
		i = each//step
		bucket[i].append(each)
		for j in range(len(bucket[i])-1, 0, -1):
			if bucket[i][j] < bucket[i][j-1]:
				bucket[i][j], bucket[i][j-1] = bucket[i][j-1], bucket[j]
			else:
				break
		while j-1>=0 and bucket[i][j] < bucket[i][j-1]:
			bucket[i][j], bucket[i][j-1] = bucket[i][j-1], bucket[j]
	i = 0
	for each in bucket:
		for every in each:
			li[i] = every
			i += 1
	sorted_li = []
	for each in bucket:
		sorted_li.extend(each)
	
	return sorted_li
			
li = [random.randint(10000) for _ in range(20)]
print(li)
bucket_sort(li)
print(li)
