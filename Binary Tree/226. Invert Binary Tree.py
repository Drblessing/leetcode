# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive DFS
        # 1. Iterate through tree
        # 2. Swap leaves
        # 3. Swap subtrees

        # Ignore empty nodes
        if not root:
            return

        # Swap subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left
        return root
