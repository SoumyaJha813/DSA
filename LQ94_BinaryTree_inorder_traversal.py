# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # non - recursive way
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        #if not root:
        #    return
        ll = []
        node = root
        while ll or node:
            if node:
                ll.append(node)
                node = node.left
            else:
                node = ll.pop()
                result.append(node.val)
                node = node.right
        return result
