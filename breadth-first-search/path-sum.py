# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right
# class Solution(object):
#     def hasPathSum(self, root, targetSum):
#         """
#         :type root: Optional[TreeNode]
#         :type targetSum: int
#         :rtype: bool
#         """
#         if not root:
#             return False 
        
#         if not root.left and not root.right:
#             return root.value == root 
        
#         new_sum = targetSum  - root.value 

#         return (self.hasPathSum(root.left, new_sum) or 
#                 self.hasPathSum(root.right, new_sum)
#         )
        
class TreeNode:
    def __init__(self, value):
        self.value = value      # value stored at this node
        self.left = None        # left child node
        self.right = None       # right child node

class Solution:
    def hasPathSum(self, current_node, target_sum):
        # If the current node is empty, there is no path
        if not current_node:
            return False

        # If we are at a leaf node, check if the value equals the remaining sum
        if not current_node.left and not current_node.right:
            return current_node.val == target_sum

        # Subtract current node's value from the target sum
        new_sum = target_sum - current_node.val

        # Recursively check left and right child paths
        return (self.hasPathSum(current_node.left, new_sum) or
                self.hasPathSum(current_node.right, new_sum))