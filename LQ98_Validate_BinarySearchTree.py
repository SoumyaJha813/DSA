# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self,root):
        currentNode = root
        if currentNode.left is None:
            return currentNode
        else:
            return self.findMin(currentNode.left)
    def findMax(self,root):
        currentNode = root
        if currentNode.right is None:
            return currentNode
        else:
            return self.findMax(currentNode.right)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if (root.right is not None and self.findMin(root.right).val == root) and (root.left is not None and self.findMax(root.left).val == root):
            return False
        if root.left is not None and self.findMax(root.left).val >= root.val:
            return False
        if root.right is not None and self.findMin(root.right).val <= root.val:
            return False
        
        if not self.isValidBST(root.left) or not self.isValidBST(root.right):
            return False
        return True
        
