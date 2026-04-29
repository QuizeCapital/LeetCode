# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        stack = [(p, q)]
        while stack:
            first_tree_node, second_tree_node = stack.pop()
            if first_tree_node or second_tree_node:
                if (not first_tree_node or 
                    not second_tree_node or
                    first_tree_node.val != second_tree_node.val):
                    return False
                
                stack.append((first_tree_node.left, second_tree_node.left))
                stack.append((first_tree_node.right, second_tree_node.right))

        return True
        