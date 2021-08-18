from collections import deque

q = deque([1,2,3,4,5], 5)
q.append(6) #队尾进队
print(q.popleft()) #队首出队

# 用于双向队列
q.appendleft(8) #队首进队
print(q.pop()) #队尾出队
print(q)

def tail(n):
    with open('test.txt', 'r') as f:
        q = deque(f, n)
        return q
for line in tail(5):
    print(line, end='')