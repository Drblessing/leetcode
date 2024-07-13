# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


def list_to_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    i = 1

    while queue and i < len(nodes):
        current = queue.pop(0)

        if i < len(nodes) and nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1

    return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root.left, 1, "l"), (root.right, 1, "r")]
        max_zig = 0

        while stack:
            node, depth, direction = stack.pop()
            if not node:
                continue
            max_zig = max(depth, max_zig)

            if direction == "l":
                stack.append([node.left, 1, "l"])
                stack.append([node.right, depth + 1, "r"])

            elif direction == "r":
                stack.append([node.right, 1, "r"])
                stack.append([node.left, depth + 1, "l"])

        return max_zig


# Test the solution
root_list = [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]
root = list_to_tree(root_list)
solution = Solution()
result = solution.longestZigZag(root)
print(f"The longest ZigZag path is: {result}")
