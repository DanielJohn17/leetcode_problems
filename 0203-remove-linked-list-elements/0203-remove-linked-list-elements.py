# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:        
        dummy = ListNode()
        temp = dummy
        while head:
            if head.val == val:
                head = head.next
            else:
                temp.next = head
                head = head.next
                temp = temp.next
                temp.next = None
        
        return dummy.next
