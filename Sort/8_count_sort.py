def count_sort(li):
    res = [0 for i in range(100)]
    for each in li:
        res[each] += 1
    j = 0
    for i in range(100):
        while res[i]>0:
            li[j] = i
            j += 1
            res[i] -= 1

li = [int(i) for i in input('Please enter the list:').split()]
print('start:',li)
count_sort(li)
print('end', li)
