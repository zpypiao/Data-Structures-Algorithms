from cal_time import *

def big_heap(li, start,  end):
	root = start
	child = root*2+1 # left child
	while child<=end:
		if child+1<=end and li[child+1]>li[child]: # search the biggest child
			child += 1
		if li[root] < li[child]:
			li[child], li[root], root = li[root], li[child], child
			child = root*2+1
		else:
			break

@cal_time			
def heap_sort(li):
	start = 0
	l = len(li)-1
	end = len(li)-1
	for i in range(l, -1, -1):
		big_heap(li, i, end)
	for i in range(l):
		li[0], li[end] = li[end], li[0]
		end-=1
		big_heap(li, 0, end)
		
		
li = [int(i) for i in input('Please enter the list:').split()]
heap_sort(li)
print(li)
