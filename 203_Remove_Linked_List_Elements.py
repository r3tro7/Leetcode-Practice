# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = head
        prev = None
        while current:
            if current.val == val:
                if prev:
                    prev.next = current.next
                else:
                    head = current.next
                # if the else statement is executed, the current becomes head, and head is already
                # current.next
                current = current.next
            else:
                prev = current
                current = current.next
        return head

# Best explanation : https://leetcode.com/problems/remove-linked-list-elements/discuss/1572935/Python-99-One-pass-Solution-with-Explanation