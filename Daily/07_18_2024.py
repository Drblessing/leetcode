# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def common_prefix(self, node_path_1, node_path_2):
        """Return the end index of the common prefix of two nodes."""
        i = 0
        n, m = len(node_path_1), len(node_path_2)
        while i < n and i < m and node_path_1[i] == node_path_2[i]:
            i += 1
        return i

    def countPairs(self, root: TreeNode, distance: int) -> int:
        """Count leaf nodes in a tree that are distance apart.
        Distance between leaf nodes = distance to LCA * 2,
        therefore we just need to find the LCA between every leaf nodes.
        This is too long, so we instead find the path to every leaf node,
        and check the first divergence, and then multipy distance by 2"""

        leaf_node_paths = []

        def _bfs(node, path, leaf_node_paths):
            if not node:
                return

            l = node.left
            r = node.right
            if not l and not r:
                leaf_node_paths.append(path)
                return

            if l:
                _bfs(l, path + "l", leaf_node_paths)

            if r:
                _bfs(r, path + "r", leaf_node_paths)

        _bfs(root, "", leaf_node_paths)

        # Compare leaf nodes
        n = len(leaf_node_paths)
        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                # Distance = len(p[i]) + len(p[j]) - common prefix
                prefix = self.common_prefix(leaf_node_paths[i], leaf_node_paths[j])
                left_path = leaf_node_paths[i][prefix:]
                right_path = leaf_node_paths[j][prefix:]
                if len(left_path) + len(right_path) <= distance:
                    result += 1
        return result
