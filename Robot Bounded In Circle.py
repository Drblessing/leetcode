class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        # Iterate through instructions 4 times
        # all emergent behavior will appear
        instructions *= 4

        # Track the steps in each direction
        d = {}
        d[0] = 0  # L
        d[1] = 0  # U
        d[2] = 0  # R
        d[3] = 0  # D

        # Init direction
        direction = 0

        # Iterate throug the steps
        # L -> direction = (direction - 1) % 4
        # R -> direction = (direction + 1) % 4
        for step in instructions:
            if step == 'G':
                d[direction] += 1

            elif step == 'L':
                direction = (direction - 1) % 4

            elif step == 'R':
                direction = (direction + 1) % 4

        # Check that it's gone net 0 distance
        return d[0] == d[2] and d[1] == d[3]






