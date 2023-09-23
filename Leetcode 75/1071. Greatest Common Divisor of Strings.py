class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Find the gcd of two strings.
        # Set str1 to smaller string.
        str1, str2 = (str1, str2) if len(str1) <= len(str2) else (str2, str1)
        # Start with longest prefix down.
        # Length will be k.
        len1, len2 = len(str1), len(str2)
        for k in range(len(str1), 0, -1):
            # Check that k is a divisor of len1 and len2
            if len1 % k != 0 or len2 % k != 0:
                continue
            # Calculate number of prefixs.
            n1, n2 = len1 // k, len2 // k
            # Check that prefix * n1 is str1 and str2.
            prefix = str1[:k]
            if prefix * n1 == str1 and prefix * n2 == str2:
                return prefix
        return ""
