# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        check = []
        tmp = head
        while head:
            check.append(head.val)
            head = head.next
        
        l = 0
        r = len(check) - 1
        while l < r:
            if check[l] != check[r]:
                return False
            l += 1
            r -= 1
        return True