# IMP Notice: here we only have access to the node to be deleted and further

# Visualization:
# [4,5,1,9] del 5
# we can't access 4 we can only access 5
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next