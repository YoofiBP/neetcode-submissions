class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        operands = {"+", "-", "*", "/"}

        endResult = None

        for i in tokens:
            if i in operands:
                right = int(stack.pop())
                left = int(stack.pop())
                result = int(self.performOperation(i, (left, right)))
                stack.append(result)
                if i == tokens[-1]:
                    endResult = result
            else:
                stack.append(i)
        
        return endResult


    def performOperation(self, operation: str, operands):
        left = operands[0]
        right = operands[1]
        if operation == "+":
            return left + right
        elif operation == "-":
            return left - right
        elif operation == "*":
            return left * right
        elif operation == "/":
            return left / right
        else:
            raise ValueError

        