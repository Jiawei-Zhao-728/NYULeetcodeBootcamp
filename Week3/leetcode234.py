# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        stack = []
        slow = fast = head

        # Move slow and fast pointers, push slow values onto the stack
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        # If odd number of elements, skip the middle
        if fast:
            slow = slow.next

        # Compare second half with the stack
        while slow:
            top = stack.pop()
            if slow.val != top:
                return False
            slow = slow.next

        return True