class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in s:
            if i != ')':
                stack.append(i)
            else:
                current=''
                while stack[-1]!='(':
                    current = current+stack.pop(-1)[::-1]
                stack.pop(-1)
                stack.append(current)
        return "".join(stack)
