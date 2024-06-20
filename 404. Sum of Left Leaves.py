# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    addition = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traversal(node,val):
            if node is None:
                return
            traversal(node.left,1)
            if val==1 and node.left is None and node.right is None:
                self.addition=self.addition+node.val
            traversal(node.right,2)
        traversal(root,2)
        return self.addition
