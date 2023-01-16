# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # Recursive dfs
        # 1. Find current root node
        # 2. Split tree into left and right trees
        # 3. Build left and right trees

        # Still nodes
        if inorder:
            # Preorder[0] is current root
            index = inorder.index(preorder.pop(0))
            # Init root
            root = TreeNode(inorder[index])
            # Build left and right trees
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index + 1 :])
            # Return for parent trees
            return root
        # Empty trees
        return None
