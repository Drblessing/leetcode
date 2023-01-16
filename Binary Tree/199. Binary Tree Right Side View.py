# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative solution
        # 1. Init queue
        # 2. On each level grab right most value

        # Empty root
        if not root:
            return []
        right_side = []
        current_level = [root]
        while current_level:
            current_level_nodes = []
            next_level = []
            for node in current_level:
                current_level_nodes.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            right_side.append(current_level_nodes)
            current_level = next_level

        return [i[-1] for i in right_side]
