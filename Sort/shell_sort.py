def shell_sort(li):
    n = len(li)
    d = n//2
    k = 1
    while d:
        for i in range(d+1, n):
            while i-d>=0 and li[i] < li[i-d]:
                li[i], li[i-d] = li[i-d], li[i]
                i -= d
        if d == 1:
            break
        d = d//2

li = [int(i) for i in input('Please enter the list:').split()]
print('start:',li)
shell_sort(li)
print('end', li)
