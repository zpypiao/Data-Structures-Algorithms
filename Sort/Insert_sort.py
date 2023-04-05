from cal_time import *

@cal_time
def insert_sort(li):
	temp = li[0]
	for i in range(1, len(li)):
		temp = li[i]
		j = i
		while j>=0:
			if temp <= li[j]:
