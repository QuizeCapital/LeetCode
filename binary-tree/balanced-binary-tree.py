# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    balanced = True
    def get_height(self, node):
        if node is None:
            return 0 
        
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        if abs(left_height - right_height) > 1:
            self.balanced = False
        
        return max(left_height, right_height) + 1
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True 
        
        self.get_height(root)
        return self.balanced
