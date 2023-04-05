from cal_time import *

@cal_time
def bubble_sort(li):
	for i in range(len(li)-1):
		for j in range(0, len(li)-i-1):
			if li[j] > li[j+1]:
				li[j], li[j+1] = li[j+1], li[j]
				
li = [int(i) for i in input('Please enter the list:').split()]
print(li)
bubble_sort(li)
print(li)
