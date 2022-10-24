# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        fast = head

        while fast and fast.next:
            current = current.next
            fast = fast.next.next
        return current

    # Initial Approach for 2 pointer
    # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     current = head
    #     fast = head
    #     while fast.next:
    #         if fast.next.next:
    #             current = current.next
    #             fast = fast.next.next
    #         else:
    #             current = current.next
    #             break
    #     return current

    # Naive Approach
    # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     current = head
    #     mid:int = (self.getLen(current) // 2) + 1
    #     for i in range(mid-1):
    #         current = current.next
    #     return current

    # def getLen(self, curr: Optional[ListNode]) -> int:
    #     count:int = 0
    #     while curr:
    #         curr = curr.next
    #         count+=1
    #     return count