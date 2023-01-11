"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        # BFS
        # 1. Iterate over nodes in a queue
        # 2. Keep a hashmap of visited nodes and their clones
        original_node = node
        if node == None:
            return node
        queue = deque([node])
        clones = {node.val: Node(node.val, [])}
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                clones[node.val].neighbors.append(clones[neighbor.val])

        return clones[original_node.val]
