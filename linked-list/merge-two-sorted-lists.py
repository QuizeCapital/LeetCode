# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        starter_node = ListNode()
        builder = starter_node

        while list1 and list2:
            if list1.val <= list2.val:
                builder.next = ListNode(list1.val)
                list1 = list1.next
            else:
                builder.next = ListNode(list2.val)
                list2 = list2.next

            builder = builder.next
        if list1:
            builder.next = list1
        elif list2:
            builder.next = list2

        return starter_node.next



