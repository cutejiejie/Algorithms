from cal_time import *

@cal_time
def radix_sort(li):
    max_num = max(li)  # 最大值 9->1, 99->2, 888->3, 10000->5
    # 迭代多少次  it=0是个位   it=1是十位 it=2是百位
    it = 0
    # 10的it倍数  10的零次方是1 1小于9  10的一次方是2次   10的2次方是100是3次  10的3次方是1000
    # 位数是几我们就做几次循环
    while 10 ** it <= max_num:
        # 分桶
        buckets = [[] for _ in range(10)]
        # 把这个元素放到几号桶
        for var in li:
            # 987 it=1  987//10=98 98%10=8; --取第二位     it=2  987//100=9 9%10=9   --取第三位    %10就是去于
            digit = (var // 10 ** it) % 10
            # 找到它对应的桶     分桶完成
            buckets[digit].append(var)

        li.clear()
        for buc in buckets:
            # 把数重新写回li
            li.extend(buc)
        # 到这又重新建桶，分桶
        it += 1


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp: #从右面找到比tmp小的数
            right -= 1 #往左走一步
        li[left] = li[right] #把右边的值写到左边空位上
        # print(li, 'right')
        while left < right and li[left] <= tmp:
            left += 1 #往左走一步
        li[right] = li[left] #把左边的值写到右边空位上
        # print(li, 'left')
    li[left] = tmp #把tmp归位
    return left
def _quick_sort(li, left, right):
    if left < right: #至少两个元素
        mid = partition(li, left, right)
        _quick_sort(li, left, mid-1)
        _quick_sort(li, mid+1, right)
@cal_time
def quick_sort(li):
    _quick_sort(li, 0, len(li) - 1)


import random, copy
# li = [random.randint(0, 100) for _ in range(100)]
# random.shuffle(li)
# print(li)
# radix_sort(li)
# print(li)
# li = list(range(100000))
li = [random.randint(0, 10000000000) for _ in range(100000)]
random.shuffle(li)
li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
li3 = copy.deepcopy(li)
quick_sort(li1) #nlogn logn=log(2,n)
radix_sort(li2) #kn k=log(10,n)