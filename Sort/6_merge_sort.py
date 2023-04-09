def merge(li, low, mid, high):
    left = low
    right = mid
    end = high
    result = []
    while left<mid and right<=end:
        if li[left]<li[right]:
            result.append(li[left])
            left += 1
        else:
            result.append(li[right])
            right+=1
    while right<=end:
        result.append(li[right])
        right += 1
    while left<mid:
        result.append(li[left])
        left += 1
    li[low: high+1] = result
    
def merge_sort(li, low, high):
    if low < high:
        mid = (low +high)//2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)
                

li = [int(i) for i in input('please enter:').split()]
merge_sort(li, 0, len(li)-1 )
print(li)
