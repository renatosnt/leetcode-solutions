# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # lnr inorder
        # nlr preorder
        # lrn posorder
        stack = []
        ans = []
        curr = root
        while curr or stack:
            # esquerda
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack[-1]
            # node
            stack.pop()
            ans.append(curr.val)
            # direita
            curr = curr.right
        return ans