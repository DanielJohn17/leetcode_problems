# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        temp = head
        temp2 = head.next

        while temp2:
            if (temp2.val == temp.val):
                temp.next = temp2.next
                temp2 = temp2.next
                continue
            temp = temp.next

        return head
        