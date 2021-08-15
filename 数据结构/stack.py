class Stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        return self.stack.pop()
    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    def is_empty(self):
        return len(self.stack) == 0

def brace_match(s):
    match = {'}':'{', ']':'[', ')':'('}
    stack =Stack()
    for ch in s:
        if ch in {'{', '[', '('}:
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
            elif stack.get_top() == match[ch]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(90)
# print(stack.pop())
# print(stack.get_top())
print(brace_match('{[]{()[]}[]()}'))
print(brace_match('[){}(]'))