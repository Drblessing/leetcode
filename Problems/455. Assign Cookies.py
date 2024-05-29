class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        satisfied_children = 0
        while s and g:
            smallest_cookie = s.pop(0)
            # Check if smallest cookie can satisfy any child
            least_greedy_child = g[0]
            if smallest_cookie >= least_greedy_child:
                g.pop(0)
                satisfied_children += 1

        return satisfied_children
