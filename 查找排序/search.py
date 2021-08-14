from cal_time import *
'''顺序查找，时间复杂度O(n)'''

@cal_time
def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            print('查找目标的索引值为:',ind)
            return ind
    else:
        return '没找到'
# linear_search([12,33,168,34,65,'jiejie',88,90], 'jiejie')

@cal_time
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right)//2
        if li[mid] > val:
            right = mid -1
        elif li[mid] < val:
            left = mid +1
        elif li[mid] == val:
            return ('找到了，目标元素的索引值为:',mid)
    else:
        return None

# print(binary_search([11,22,24,33,36,44,48,55,66],88))

li = list(range(10000000))
linear_search(li, 3890)
binary_search(li, 3890)

