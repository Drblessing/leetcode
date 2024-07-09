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
                chef_available_time += time
                waiting_time += time
            # Chef is working, have to start when he's done
            if chef_available_time > arrive:
                chef_available_time += time
                waiting_time = chef_available_time - arrive

        return waiting_time / n
