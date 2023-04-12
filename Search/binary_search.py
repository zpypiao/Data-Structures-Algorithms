from cal_time import *

@cal_time
def binary_search(li, val):
	left = 0
	right = len(li) - 1
	key = False
	while left <= right:
		mid = (left + right)//2
		if li[mid] < val:
			left = mid + 1
		elif li[mid] > val:
			right = mid - 1
		else:
			key = True
			break
	return key

li = [int(i) for i in input().split()]

val = int(input('Please enter a int'))

answer = binary_search(li, val)

print(answer)
