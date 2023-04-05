from cal_time import *

@cal_time
def select_sort(li):
	for i in range(len(li)):
		mv = li[i]
		l = i
		for j in range(i, len(li)):
			if li[j] < mv:
				mv = li[j]
				l = j
		li[i], li[l] = li[l], li[i]
		
li = [int(i) for i in input('Please enter the list you want to sort:').split()]
print(li)
select_sort(li)
print(li)
