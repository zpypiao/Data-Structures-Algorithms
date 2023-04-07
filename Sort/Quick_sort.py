from cal_time import *

def once_sort(li, left, right):
	mid = (left+right)//2
	temp = li[mid]
	while left < right:
		while True:
			if li[left]<temp:
				left += 1
			else:
				break
		while True:
			if li[right] > temp:
				right -= 1
			else:
				break
		li[left], li[right] = li[right], li[left]
	li[left] = temp
	return left
			

@cal_time
def quick_sort(li, left, right):
	if left<right:
		k = once_sort(li, left, right)
		quick_sort(li, left, k-1)
		quick_sort(li, k+1, right)
	else:
		return None
		
li = [int(i) for i in input('Please enter the list:').split()]
quick_sort(li)
print(li)

# this is wrong, it is waitting to be rectified.
