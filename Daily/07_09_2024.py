from typing import List
import unittest


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        """
        Calculates the average waiting time for a list of customers in a single-threaded (sequential) scenario.

        Each customer is represented as [arrival_time, order_time]. The function computes the average
        waiting time for all customers.

        Parameters:
        customers (List[List[int]]): A list of customers, where each customer is represented as
                                     [arrival_time, order_time].

        Returns:
        float: The average waiting time for all customers.
        """
        cum_wait_tim = 0
        next_idle_time = 0
        for arrival_time, order_time in customers:
            # Calculate the next time the chef can start cooking this order
            next_idle_time = max(next_idle_time, arrival_time) + order_time
            # Add the wait time for this customer (finish time - arrival time)
            cum_wait_tim += next_idle_time - arrival_time

        # Calculate and return the average wait time
        return cum_wait_tim / len(customers)


# Test cases using unittest
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        customers = [[1, 2], [2, 5], [4, 3]]
        expected = 5.00000
        result = self.solution.averageWaitingTime(customers)
        self.assertAlmostEqual(result, expected, places=5)

    def test_case_2(self):
        customers = [[5, 2], [5, 4], [10, 3], [20, 1]]
        expected = 3.25000
        result = self.solution.averageWaitingTime(customers)
        self.assertAlmostEqual(result, expected, places=5)


# Run unittest when executing this file directly
if __name__ == "__main__":
    unittest.main(verbosity=2)
