class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Stack
        # 1. Add numbers to stack
        # 2. When finding a token, pop
        # two numbers off of stack
        # 3. Add computation back to stack
        # 4. Continue until tokens are empty

        symbols = ["+", "-", "*", "/"]
        stack = []
        while len(tokens) > 0:
            symbol = tokens.pop(0)
            if symbol in symbols:
                # Pop two off
                operand_2, operand_1 = int(stack.pop()), int(stack.pop())
                if symbol == "+":
                    new_symbol = operand_1 + operand_2
                elif symbol == "-":
                    new_symbol = operand_1 - operand_2
                elif symbol == "*":
                    new_symbol = operand_1 * operand_2
                elif symbol == "/":
                    new_symbol = operand_1 / operand_2
                stack.append(str(int(new_symbol)))
            else:
                stack.append(symbol)
        return int(stack[0])
