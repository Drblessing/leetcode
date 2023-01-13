class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topological sort BFS
        # 1. Create graph with inDegree
        # 2. Iterate through source nodes
        # 3. Check if we've visited everynode

        graph = defaultdict(list)
        inDegree = [0 for _ in range(numCourses)]
        sources = deque()

        for adj, node in prerequisites:
            graph[node].append(adj)
            inDegree[adj] += 1

        for node, degree in enumerate(inDegree):
            if degree == 0:
                sources.append(node)
        visited = 0
        while sources:
            node = sources.popleft()
            visited += 1
            for adj in graph[node]:
                inDegree[adj] -= 1
                if inDegree[adj] == 0:
                    sources.append(adj)

        return visited == numCourses
