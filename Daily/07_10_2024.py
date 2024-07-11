from typing import List
import unittest


class Solution:
    BASE = "."
    STARTING_DEPTH = 0
    MAX_LOG_LENGTH = 10

    @staticmethod
    def is_valid_operation(log: str) -> bool:
        """Verify that the log is a valid operation."""
        if (log == "./") or (log == "../"):
            return True
        # Log too long
        elif len(log) > Solution.MAX_LOG_LENGTH:
            return False
        # Valid folder
        elif (
            (log[:-1].islower() or log[:-1].isdigit())
            and log[:-1].isalnum()
            and log[-1] == "/"
        ):
            return True

        return False

    def minOperations(self, logs: List[str]) -> int:
        """Calculate the number of operations needed to
        return to the main folder."""

        if not logs:
            return 0
        # Iterate through logs and keep track of depth
        depth = Solution.STARTING_DEPTH
        for log in logs:
            if not Solution.is_valid_operation(log):
                raise ValueError(f"Invalid log: {log}")

            if log == "./":
                continue

            elif log == "../":
                # Depth cannot go below 0
                depth = max(depth - 1, 0)

            else:
                depth += 1

        return depth


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minOperations(self):
        self.assertEqual(
            self.solution.minOperations(["d1/", "d2/", "../", "d21/", "./"]), 2
        )
        self.assertEqual(
            self.solution.minOperations(["d1/", "d2/", "./", "d3/", "../", "d31/"]), 3
        )
        self.assertEqual(self.solution.minOperations(["d1/", "../", "../", "../"]), 0)

    def test_empty_logs(self):
        self.assertEqual(self.solution.minOperations([]), 0)

    def test_error_logs(self):
        self.assertRaises(
            ValueError, self.solution.minOperations, ["invalid/operation"]
        )
        self.assertRaises(
            ValueError, self.solution.minOperations, ["./", "invalid/operation"]
        )


if __name__ == "__main__":
    unittest.main()
