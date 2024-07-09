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
            # The chef will start cooking the order at the maximum of the current time and the arrival time of the customer
            # i.e., either the chef is free when the customer arrives, or the chef is busy with another customer.
            # The chef cannot start an order before the arrival time of the customer.
            next_idle_time = max(next_idle_time, arrival_time) + order_time
            # next_idle_time becomes the time the chef finishes the order for the current customer
            # the wait time ies the finish time - arrival time
            cum_wait_tim += next_idle_time - arrival_time
        return cum_wait_tim / len(customers)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        customers = [[1, 2], [2, 5], [4, 3]]
        expected = 5.00000
        self.assertAlmostEqual(
            self.solution.averageWaitingTime(customers), expected, places=5
        )

    def test_case_2(self):
        customers = [[5, 2], [5, 4], [10, 3], [20, 1]]
        expected = 3.25000
        self.assertAlmostEqual(
            self.solution.averageWaitingTime(customers), expected, places=5
        )

    def test_dummy(self):
        # Assert 2 == 2
        self.assertEqual(2, 2)


if __name__ == "__main__":
    unittest.main()
