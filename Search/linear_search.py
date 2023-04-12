from cal_time import *

@cal_time
def linear_search(li, val):
	for ind, v in enumerate(li):
		if each == val:
			return True
	else:
		reurn False
		
		
m = list(input().split())

val = double(input())

answer = linear_search(m, val)

print(answer)
