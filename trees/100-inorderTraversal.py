# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = [True]
        def dfs(n1, n2):
            
            if not n1 and not n2:
                return

            if not n1 or not n2:
                ans[0] = False
                return
            
            dfs(n1.left, n2.left)
            print(n1.val, n2.val)
            if n1.val != n2.val:
                ans[0] = False
            dfs(n1.right, n2.right)

        dfs(p, q)
        return ans[0]