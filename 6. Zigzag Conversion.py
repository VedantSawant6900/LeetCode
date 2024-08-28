class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans=["" for _ in range(numRows)]
        pointer=0
        direction=1
        for i in s:
            ans[pointer]=ans[pointer]+i
            pointer+=direction
            if pointer<0:
                pointer = 1
                direction = 1
            elif pointer==numRows:
                pointer=pointer-2
                direction = -1
        return "".join(ans)