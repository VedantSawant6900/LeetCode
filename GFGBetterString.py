class Solution:
    def betterString(self, str1, str2):
        str1d={}
        l1=len(str1)
        str2d={}
        l2=len(str2)
        def count(ind,s,d,l,st):
            if s not in d:
                d[s]=1
            if ind>=l:
                return
            count(ind+1,s+st[ind],d,l,st)
            count(ind+1,s,d,l,st)
        count(0,"",str1d,l1,str1)
        count(0,"",str2d,l2,str2)
        print(str1d,len(str1d))
        print(str2d,len(str2d))
        return str1 if len(str1d)>=len(str2d) else str2
obj=Solution()
print(obj.betterString("sqapzwbb","ljmolmti"))