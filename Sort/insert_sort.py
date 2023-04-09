from cal_time import *

@cal_time
def insert_sort(li):
	for i in range(1, len(li)):
		temp = li[i]
		j = i-1
		while j>=0:
			if temp >= li[j]:
				li[j+1] = temp
				break
			else:
				li[j+1] = li[j]
			j -= 1
		if j == -1:
			li[0] = temp
			
li = [int(i) for i in input('Please enter the list you want to sort:').split()]
print(li)
insert_sort(li)
print(li)
