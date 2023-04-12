from cal_time import *

def once_sort(li, left, right):
    temp = li[left]
    while left < right:
		while li[right]>=temp and left<right:
			right -= 1
		li[left] = li[right]
        while li[left]<=temp and left < right:
            left += 1
        li[right] = li[left]
    li[left] = temp
    return left
            
@cal_time
def quick_sort(li, left, right):
    if left < right:
        k = once_sort(li, left, right)
        quick_sort(li, left, k-1)
        quick_sort(li, k+1, right)

li = [int(i) for i in input('Please enter the list you want to sort:').split()]
print(li)
quick_sort(li, 0, len(li)-1)
print(li)
