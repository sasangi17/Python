class Solution(object):

    def evalRPN(self, tokens):
        stack = []

        for token in tokens:

            if token in ["+", "-", "*", "/"]:
                right = stack.pop()
                left = stack.pop()

                if token == "+":
                    stack.append(left + right)

                elif token == "-":
                    stack.append(left - right)

                elif token == "*":
                    stack.append(left * right)

                elif token == "/":
                    result = abs(left) // abs(right)

                    if (left < 0) != (right < 0):
                        result = -result

                    stack.append(result)

            else:
                stack.append(int(token))

        return stack[-1]