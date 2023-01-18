class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Min heap
        # 1. Iterate through points, adding them to min heap
        # 2. Pop k items from min heap

        # Create heap and add all points
        min_heap = []
        for x, y in points:
            distance = (x**2 + y**2) ** (1 / 2)
            heappush(min_heap, (distance, (x, y)))

        # Access kth elements
        k_points = []
        for i in range(k):
            k_points.append(heappop(min_heap)[1])
        return k_points
