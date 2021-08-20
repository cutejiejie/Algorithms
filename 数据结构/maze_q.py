from collections import deque
maze = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
[1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
[1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x,y: (x, y - 1),
    lambda x,y: (x + 1, y),
    lambda x,y: (x, y + 1),
    lambda x,y: (x - 1, y)
]

def print_r(path):
    cur_node = path[-1]
    real_path = []
    while cur_node[2] != -1:
        real_path.append(cur_node[0:2])
        cur_node = path[cur_node[2]]
    real_path.append(cur_node[0:2])
    real_path.reverse()
    for node in real_path:
        print(node)



def maze_path_queue(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1, -1))
    path = []
    # 队空了，没有路
    while len(queue) > 0:
        cur_node = queue.popleft()
        path.append(cur_node)
        if cur_node[0] == x2 and cur_node[1] == y2:
            print_r(path)
            return True

        for dir in dirs:
            next_node = dir(cur_node[0], cur_node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                # 后续节点进队，记录哪个节点带它来的
                queue.append((next_node[0], next_node[1], len(path)-1))
                maze[next_node[0]][next_node[1]] = 2

    else:
        print("走投无路，无路可走")
        return False

maze_path_queue(1, 1, 8, 8)
