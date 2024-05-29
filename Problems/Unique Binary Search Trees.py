class Solution:
    def numTrees(self, n: int) -> int:

        # Calculation through induction
        # G(3) = G(2)*G(0) + G(1)*(G1) + G(0)*G(2)
        G = {}

        G[0] = 1
        G[1] = 1

        # need G(n-1) to calcualte G(n)
        for i in range(2, n + 1):

            s = 0
            for j in range(0, i):
                # sum of G's need to be i-1
                s += G[j] * G[i - j - 1]
            G[i] = s
        return G[n]