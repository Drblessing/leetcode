# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        """Create a binary tree from the given list of descriptions.
        Return the root of the binary tree.
        """

        # Create a dictionary to store the TreeNode objects
        # Each value is unique and the key is the value of the TreeNode
        tree_nodes = {}

        # Create the TreeNode objects
        for description in descriptions:
            # Extract the values from the description
            value, child, isLeft = description

            # Create the TreeNode object
            if value not in tree_nodes:
                tree_nodes[value] = TreeNode(value)
            node = tree_nodes[value]

            # Create the child TreeNode object
            if child not in tree_nodes:
                tree_nodes[child] = TreeNode(child)
            child_node = tree_nodes[child]

            # Set the child node to the left or right of the parent node
            if isLeft:
                node.left = child_node
            else:
                node.right = child_node

        # The root of the binary tree is the node with no parent
        nodes_with_parent = set()
        for value, node in tree_nodes.items():
            if node.left:
                nodes_with_parent.add(node.left.val)
            if node.right:
                nodes_with_parent.add(node.right.val)

        root = list(set(tree_nodes.keys()) - nodes_with_parent)[0]

        return tree_nodes[root]


descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
print(Solution().createBinaryTree(descriptions))
