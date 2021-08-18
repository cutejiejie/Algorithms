'''思路：从起点开始按照顺序寻找路径，通过栈记录已经走过的路径。如果最后发现不通就返回上一步，换个方向继续寻找
深度优先'''

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


dirs = [
    lambda x, y: (x+1, y),
    lambda x, y: (x-1, y),
    lambda x, y: (x, y-1),
    lambda x, y: (x, y+1)
]
def maze_path(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    while (len(stack) > 0):
        curNode = stack[-1] #当前的节点，curNode是长度为2的元组
        if curNode[0] == x2 and curNode[1] == y2:
            # 走到终点了
            for p in stack:
                print(p)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                # 找到了下一个
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2  # 标记为已经走过，防止死循环
                break
        else: #四个方向都没找到
            maze[nextNode[0]][nextNode[1]] == 2
            stack.pop() #回溯
    else:
        print('没有路')
        return False

maze_path(1,1,8,8)


