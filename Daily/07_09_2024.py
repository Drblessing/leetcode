from typing import List
import pytest


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        """Calculate the average waiting time of processes
        given a single thread, or chef."""

        # Iterate through the customers, checking if the chef
        # is available, and calculating the wait time

        # Init variables
        n = len(customers)
        waiting_time = 0
        chef_available_time = 1
        # Check for customers
        for arrive, time in customers:
            # Chef is available when customer arrives
            if chef_available_time <= arrive:
                chef_available_time = arrive + time
                waiting_time += time
            # Chef is working, have to start when he's done
            else:
                chef_available_time += time
                waiting_time += chef_available_time - arrive

        return waiting_time / n


def test_averageWaitingTime():
    solution = Solution()
    test_cases = [
        {"input": [[1, 2], [2, 5], [4, 3]], "expected": 5.0},
        {"input": [[5, 2], [5, 4], [10, 3], [20, 1]], "expected": 3.25},
        {"input": [[2, 6], [6, 1], [7, 3]], "expected": 4.6666666666667},
    ]

    for case in test_cases:
        assert (
            abs(solution.averageWaitingTime(case["input"]) - case["expected"]) < 1e-5
        ), f"Failed on input: {case['input']}"


# Run the test function
test_averageWaitingTime()
