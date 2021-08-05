def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new

def select_sort(li):
    for i in range(len(li) - 1): #第i趟
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
        print('第{0}趟'.format(i),li)

li = [8, 3, 4, 7, 2, 1, 9, 5, 6]
# select_sort(li)
print(select_sort_simple(li))
