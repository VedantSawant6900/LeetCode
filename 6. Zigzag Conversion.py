class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans=[]
        pivot_value = (numRows-1)*2
        addition = [pivot_value,0]
        for i in range(numRows):
            ans.append("")
            if i==0 or i == numRows-1:
                for z in range(i,len(s),pivot_value):
                    ans[i]=ans[i]+s[z]
            else:
                z=i
                while z < len(s):
                    ans[i]+=s[z]
                    z=z+addition[0]
                    if z >= len(s):
                        break
                    ans[i]+=s[z]
                    z=z+addition[1]
            addition[0]=addition[0]-2
            addition[1]=addition[1]+2
        return "".join(ans)