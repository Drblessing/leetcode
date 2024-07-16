# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """Return the right side view of a binary tree.
        bfs solution."""

        # Store bfs results in a dict
        result = {}

        def _bfs(node, depth):
            # Base case
            if not node:
                return
            # Check if depth is in result
            if depth not in result:
                result[depth] = node.val
            # bfs right subtree
            _bfs(node.right, depth + 1)
            _bfs(node.left, depth + 1)

        _bfs(root, 0)

        return result.values()
