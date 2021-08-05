import random
def bubble_sort(li):
    for i in range(len(li) - 1): #第i趟
        isexchange = False
        for j in range(len(li) - i -1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                isexchange = True
        if not isexchange:
            # break
            return
        print('第{0}趟:'.format(i),li)

li = [0, 1, 2, 3, 4, 9, 5, 7, 6, 8]
# li1 = [random.randint(0,9) for i in range(10)]
print('原列表:',li)
bubble_sort(li)

