"""
Design a stack that supports push, pop, top, and retrieving the minimum element 
in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

# use 2 stacks
# 4 2 8 2 5 7 1
# 4 2 2 1


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [float("inf")]

    def push(self, x):
        if x <= self.min_stack[-1]:
            self.min_stack.append(x)
        self.stack.append(x)

    def pop(self):
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop() # del self.min_stack[-1]
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.top())    # return 0
print(minStack.getMin()) # return -2