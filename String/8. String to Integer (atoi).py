class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. Strip whitespace and characters
        # 2. Check sign
        # 3. Read number
        s = s.strip()
        if len(s) == 0:
            return 0
        sign = False
        if s[0] == "-":
            sign = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        ss = ""
        i = 0
        while i < len(s) and s[i].isnumeric():
            ss += s[i]
            i += 1

        if not ss:
            return 0

        num = -int(ss) if sign else int(ss)

        if num < -(2**31):
            num = -(2**31)
        elif num > 2**31 - 1:
            num = 2**31 - 1
        return num
