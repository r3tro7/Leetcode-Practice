# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Postorder Traversal, Recursive Solution, O(d) space d=depth of tree
        if root is None:
            return None
        
        # temp = root.left
        # root.left = root.right
        # root.right = temp
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

        # BFS, Iterative
        # queue = [root]
        # while queue:
        #     current = queue.pop(0)
        #     if current is None:
        #         continue
        #     current.left , current.right = current.right, current.left
        #     queue.append(current.left)
        #     queue.append(current.right)
        # return root