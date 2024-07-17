# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        """Delete nodes from a binary tree and return the resulting forest."""
        to_delete_set = set(to_delete)
        forest = []

        def _postorder_traversal(node):
            if not node:
                return

            node.left = _postorder_traversal(node.left)
            node.right = _postorder_traversal(node.right)

            if node.val in to_delete_set:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None

            else:
                return node

        if _postorder_traversal(root):
            forest.append(root)
        return forest
