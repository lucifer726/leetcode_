class Solution:
    def isValid(self , s: str) -> bool:
        # write code here
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif c == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            elif c == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
        return len(stack) == 0