# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        count = defaultdict(int)

        temp = head
        while temp:
            count[temp.val] += 1
            temp = temp.next
        
        dummy = ListNode()
        temp = dummy

        while head:
            if count[head.val] == 1:
                temp.next = head
                temp = temp.next
            head = head.next
        
        temp.next = None

        return dummy.next