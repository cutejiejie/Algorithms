def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i<=mid and j<=high: #只要左右两边都有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        if li[i] > li[j]:
            ltmp.append(li[j])
            j += 1
    # while执行完，肯定有一部分没数了
    while i<=mid:
        ltmp.append(li[i])
        i += 1
    while j<=high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1]=ltmp
    return li
def merge_sort(li, low, high):
    mid = (low + high)//2
    if low<high:
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)
    return li



li=[52,34,68,12,61,83,49,26,57,60]
print(merge_sort(li, 0, len(li)-1))

