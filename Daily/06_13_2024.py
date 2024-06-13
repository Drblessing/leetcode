class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        c = 0
        for i in range(len(seats)):
            c += abs(seats[i] - students[i])
        return c
