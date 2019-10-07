# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # idea to traverse in both directions and store values in arrays
        node = head
        h = []
        while node != None:
            h.append(node.val)
            node = node.next
        h_reverse = h[::-1]
        if h == h_reverse:
            return True
        else:
            return False
