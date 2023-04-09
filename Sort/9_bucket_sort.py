import random

def bucket_sort(li, n=100, max_num=10000):
	step = max_num//n
	bucket = [[] for _ in range(n)]
	for each in li:
		i = each//step
		bucket[i].append(each)
		j = len(bucket[i])-1
		while j-1>=0 and bucket[i][j] < bucket[i][j-1]:
			bucket[i][j], bucket[i][j-1] = bucket[i][j-1], bucket[j]
	i = 0
	for each in bucket:
		for every in each:
			li[i] = every
			i += 1
			
li = [random.randint(10000) for _ in range(20)]
print(li)
bucket_sort(li)
print(li)
