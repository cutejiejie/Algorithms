class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0 #队尾指针
        self.front = 0 #队首指针
    def push(self, element): #入队
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError('Queue is filled.')
    def pop(self):#出队
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty.")
    # 判断队空
    def is_empty(self):
        return self.rear == self.front
    # 判断队满
    def is_filled(self):
        return (self.rear + 1) % self.size == self.front
q = Queue(6)
for i in range(4):
    q.push(i)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
# print(q.pop())
q.push(4)
print(q.pop())
# class Queue:
#     def __init__(self, size=100):
#         self.queue = [0 for _ in range(size)]
#         self.size = size
#         self.rear = 0  # 队尾指针
#         self.front = 0 # 队首指针
#
#     def push(self, element):#入队
#         if not self.is_filled():
#             self.rear = (self.rear + 1) % self.size
#             self.queue[self.rear] = element
#         else:
#             raise IndexError("Queue is filled.")
#
#     def pop(self):#出队
#         if not self.is_empty():
#             self.front = (self.front + 1) % self.size
#             return self.queue[self.front]
#         else:
#             raise IndexError("Queue is empty.")
#
#     # 判断队空
#     def is_empty(self):
#         return self.rear == self.front
#
#     # 判断队满
#     def is_filled(self):
#         return (self.rear + 1) % self.size == self.front
#
#
# q = Queue(51) #长度为51的队列,只能容纳50个数字,因为自己设定的,队首和队尾之间要保持一个空格,否则无法判断是空还是满
# for i in range(50):
#     q.push(i)
# print(q.pop())
# print(q.pop())
# print(q.pop())
# print(q.pop())
# q.push(4)