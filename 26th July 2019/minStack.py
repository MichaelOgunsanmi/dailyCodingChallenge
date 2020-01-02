# Source: https://leetcode.com/problems/min-stack/

# Level: Easy

# Date: 26th July, 2019


# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
#
# Example:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minVal = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.minVal.append(x)
        self.minVal.sort(reverse=True)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.minVal[len(self.minVal) - 1]:
            self.minVal.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minVal[len(self.minVal) - 1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
