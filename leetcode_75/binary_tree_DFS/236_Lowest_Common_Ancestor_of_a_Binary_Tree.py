# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """Return the lowest common ancestor (LCA) of a binary tree."""
        # Return none if recursion base case of none leaf or
        # one of the target nodes
        if not root or root == p or root == q:
            return root

        # Recurisvely call the function on the left and right subtrees
        # searching for p and q
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # If a node is found in both subtrees,
        # then we are at the LCA
        if l and r:
            return root

        # If only one subtree returns, then return it and pass it up,
        # it is either the LCA or one node we need to pass up
        elif l or r:
            # short circuiting
            return l or r

        # Both l and r are none, which means we are
        # in a branch that has neither target nodes
        else:
            return
