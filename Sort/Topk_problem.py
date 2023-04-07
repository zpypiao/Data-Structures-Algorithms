import random

def sift(li, low, high):
	i = low
	j = 2*i+1
	while j<=high:
		if j+1<=high and li[j+1]<li[j]:
			j += 1
		if li[i]>li[j]:
			li[i], li[j], i = li[j], li[i], j
			j = 2*i+1
		else:
			break
			
def heap1_sort(li):
	high = len(li)-1
	end = len(li)-1
	for i in range((high-1)//2, -1, -1):
		sift(li, i, high)
	for i in range(high+1):
		li[0], li[end] = li[end], li[0]
		end-=1
		sift(li, 0, end)
		
li = list(i for i in range(10000))

random.shuffle(li)
print(li)
k = 10
heap1_sort(li[:10])

for i in range(10, len(li)):
	if li[i]>li[0]:
		li[0] = li[i]
		sift(li, 0, 9)
		
for each in li[:10]:
	print(each)
