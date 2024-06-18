# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def traversal(node):
            res=[]
            if node is None:
                return []
            res+=traversal(node.left)
            res.append(node.val)
            res+=traversal(node.right)
            return res
        trav=traversal(root)
        minDiff=float('inf')
        for i in range(len(trav)-1):
            minDiff=min(minDiff,abs(trav[i]-trav[i+1]))
        return minDiff
