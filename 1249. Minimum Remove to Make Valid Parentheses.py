class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        p=[]
        r=[]
        for i,ele in enumerate(s):
            if ele == '(':
                p.append(i)
            elif ele == ')':
                if p:
                    p.pop()
                else:
                   r.append(i)
        com=r+p
        com.sort(reverse=True)
        for i in com:
            s=s[:i]+s[i+1:]
        return s