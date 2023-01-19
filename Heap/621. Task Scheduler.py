class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Min Heap
        # 1. Iterate through tasks
        # 2. Add them to min heap with time
        # 3. Pop off min heap until empty

        # Create a heap with max number of elements as root
        time, heap = 0, []
        for key, value in Counter(tasks).items():
            # Max heap
            heappush(heap, (-1 * value, key))

        # Iterate through tasks
        while heap:
            interval, tmp = 0, []
            while interval <= n:
                time += 1
                # Complete one of each task remaining during interval
                if heap:
                    # Can only complete one of each task per interval
                    count, task = heappop(heap)
                    # More than one task
                    if count != -1:
                        # Complete task and remove it form heap
                        tmp.append((count + 1, task))
                    # Else all of that task is completed

                # No more tasks
                if not heap and not tmp:
                    break
                else:
                    interval += 1
            # Add each completed task this interval back to heap with one less count
            [heappush(heap, task) for task in tmp]
        return time
