class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for i in logs:
            if i == "../":
                depth= depth-1 if depth>0 else 0
            elif i == "./":
                continue
            else:
                depth+=1
        return depth if depth >0 else 0
