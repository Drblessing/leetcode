class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Topological sorting
        # 1. Create graph from edges
        # 2. Iterate through leaves
        # 3. Trim leaves and find new leaves
        # 4. Continue until less than 3 leaves 

        # Edge cases, every node is a leaf
        if n <= 2:
            return [i for i in range(n)]

        # Make graph
        graph = defaultdict(set)
        for x,y in edges:
            graph[x].add(y)
            graph[y].add(x)
        
        # Grab leaves
        leaves = [x for x in graph if len(graph[x]) == 1]

        # Trim leaves
        remaining_nodes = n
        while remaining_nodes > 2:        
            new_leaves = []
            remaining_nodes -= len(leaves)
            while leaves:
                leaf = leaves.pop()
                # Check neighbors for leaves
                for neighbor in graph[leaf]:
                    graph[neighbor].discard(leaf)
                    if len(graph[neighbor]) == 1:
                        new_leaves.append(neighbor)
            leaves = new_leaves
        # Found centroieds
        return leaves