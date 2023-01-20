class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Can't turn into binary because 10^4 string limit
        # 1. Pad shorter word to length of longer word
        # 2. Start a 0 digit adding numbers
        # 3. If two ones carry the one

        # Degen case
        if a == "0" and b == "0":
            return "0"

        # Fix lengths
        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        elif len(b) < len(a):
            b = "0" * (len(a) - len(b)) + b

        # Iterate backwards, or, smallest to largest
        a, b = a[::-1], b[::-1]

        carry = 0
        s = ""
        # Iterate over digits
        for i in range(len(a)):
            if a[i] == "1" and b[i] == "1" and carry:
                s += "1"
                carry = 1
            elif a[i] == "1" and b[i] == "1":
                s += "0"
                carry = 1
            elif (a[i] == "1" and carry) or (b[i] == "1" and carry):
                s += "0"
                carry = 1
            elif a[i] == "1" or b[i] == "1" or carry:
                s += "1"
                carry = 0
            else:
                s += "0"
                carry = 0
        # If extra 1
        # Reverse for largest first
        if carry:
            return "1" + s[::-1]
        else:
            return s[::-1]
