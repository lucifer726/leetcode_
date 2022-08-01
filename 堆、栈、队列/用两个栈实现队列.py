class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        # 将第一个栈中内容弹出放入第二个栈中
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        # 第二个栈栈顶就是最先进来的元素，即队首
        res = self.stack2.pop()
        # 再将第二个栈的元素放回第一个栈
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return res
