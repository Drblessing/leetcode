# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.pair_count = 0

        def dfs(node):
            if not node:
                return {}

            if not node.left and not node.right:
                return {1: 1}  # Leaf node: distance 1, count 1

            left = dfs(node.left)
            right = dfs(node.right)

            # Count pairs
            for l_dist, l_count in left.items():
                for r_dist, r_count in right.items():
                    if l_dist + r_dist <= distance:
                        self.pair_count += l_count * r_count

            # Prepare current node's distance map
            current = defaultdict(int)
            for dist, count in left.items():
                current[dist + 1] = count
            for dist, count in right.items():
                current[dist + 1] += count

            return current

        dfs(root)
        return self.pair_count
