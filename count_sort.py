from cal_time import *

@cal_time
def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count+1)] # 生成一个值全为0长度为100+1的列表
    for val in li: # 遍历li列表的值
        count[val] += 1 # 值对应count列表下标，遍历到便执行加1
    # 这样设计也限制了不能用大于100的数字进行排序，因为超出了index下标的范围
    li.clear() # 列表清空
    for ind, val in enumerate(count): # 下标、值
        for i in range(val): # 遍历值（对应下标的统计次数）
            li.append(ind) # 将下标值添加到li列表中（统计了几次就添加几次）


@cal_time
def sys_sort(li):
    li.sort()

import random, copy
li = [random.randint(0, 100) for _ in range(1000000)]
li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
count_sort(li1)
sys_sort(li2)
"""
count_sort running time: 0.0277559757232666 secs.
sys_sort running time: 0.02849888801574707 secs.
"""
