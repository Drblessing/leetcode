# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Iterative stack solution
        # 1. Iterate over level
        # 2. On each level, record nodes
        # 3. Add new nodes to the stack

        # Empty node
        if not root:
            return []

        level_order = []
        # Start with root
        current_level = [root]
        # Iterate over all nodes
        while current_level:
            # Empty current level nodes
            current_level_nodes = []
            next_level_nodes = []
            # Go through all the nodes
            for node in current_level:
                # Append nodes to current level
                current_level_nodes.append(node.val)
                # Check for next level nodes in order
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            # Append to level order and check next level
            level_order.append(current_level_nodes)
            current_level = next_level_nodes
        return level_order
