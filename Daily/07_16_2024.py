# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirection(self, node, val, path):
        """Get direction to a node in a tree."""

        if not node:
            return False

        if node.val == val:
            return True

        if self.getDirection(node.left, val, path):
            path.append("L")
            return True
        if self.getDirection(node.right, val, path):
            path.append("R")
            return True

        return False

    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        """Get direction froms start to dest."""

        start_path = []
        self.getDirection(root, startValue, start_path)
        dest_path = []
        self.getDirection(root, destValue, dest_path)
        start_path.reverse()
        dest_path.reverse()

        # Strip common ancestors from start and dest
        while start_path and dest_path and start_path[0] == dest_path[0]:
            start_path.pop(0)
            dest_path.pop(0)

        # Turn start path into "U"
        for i in range(len(start_path)):
            start_path[i] = "U"

        return "".join(start_path + dest_path)
