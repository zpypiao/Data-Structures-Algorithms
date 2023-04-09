import random

def radix_sort(li, s=1):
	if s == 0:
		return li
	else:
		s2 = s//10
		li = radix_sort(li, s2)
		bucket = [[] for _ in range(10)]
		for each in li:
			bucket[each//s-(each//(s*10))*10].append(each)
		sorted_li = []
		for each in bucket:
			sorted_li.extend(each)
		return sorted_li
	
li = [random.randint(0, 10000) for _ in range(100)]
print(li)
li = radix_sort(li, 10000)
print(li)
