from typing import List
from collections import deque
from dataclasses import dataclass


@dataclass
class Robot:
    position: int
    health: int
    direction: str
    index: int


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        # Preprocess input data into Robot objects
        robots = [
            Robot(p, h, d, i)
            for i, (p, h, d) in enumerate(zip(positions, healths, directions))
        ]
        robots.sort(key=lambda r: r.position)  # Sort robots by position

        stack = deque()

        for robot in robots:
            if robot.direction == "R":
                stack.append(robot)
            else:  # 'L' direction
                while stack and robot.health > 0:
                    opponent = stack.pop()
                    if opponent.health > robot.health:
                        # Opponent survives
                        # Update health and add back to stack
                        opponent.health -= 1
                        stack.append(opponent)
                        robot.health = 0
                    elif opponent.health < robot.health:
                        robot.health -= 1
                        opponent.health = 0
                    else:  # Equal health
                        robot.health = 0
                        opponent.health = 0
        # Return healths in the order of the original input, that have health > 0
        survivors = [0] * len(robots)
        for robot in robots:
            survivors[robot.index] = robot.health

        return [h for h in survivors if h > 0]
