# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """

        # Step 1: Find the middle of the list:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2 Reverse the second half of the list: 
        prev = None
        curr = slow.next
        slow.next = None

        while curr: 
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # the mverging
        first, second = head, prev

        while second: 
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

        
