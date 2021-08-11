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


import random#

li = [random.randint(0, 100) for _ in range(100)]
random.shuffle(li)
print(li)
radix_sort(li)
print(li)
