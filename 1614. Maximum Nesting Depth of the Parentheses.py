class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=0
        c=0
        for i in s:
            if i=='(':
                c+=1
            elif i==')':
                c-=1
            if c>maxi:
                maxi=c
        return maxi