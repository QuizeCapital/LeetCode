# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        # If the list is empty, return None
        if not nums:
            return None

        # Middle element is the root
        mid = (len(nums) - 1) // 2
        root = TreeNode(nums[mid])

        # Stack holds (start, end, parent, is_left_child)
        stack = [
            (0, mid - 1, root, True),
            (mid + 1, len(nums) - 1, root, False)
        ]

        while stack:
            start, end, parent, is_left = stack.pop()
            if start > end:
                continue

            mid = (start + end) // 2
            node = TreeNode(nums[mid])

            if is_left:
                parent.left = node
            else:
                parent.right = node

            stack.append((start, mid - 1, node, True))
            stack.append((mid + 1, end, node, False))

        return root
