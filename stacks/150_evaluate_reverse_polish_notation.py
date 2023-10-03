from typing import List, Set

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators: Set[str] = set(["+", "-", "*", "/"])
        stack: List[int] = list()
        for token in tokens:
            if token in operators:
                right: int = stack.pop()
                left: int = stack.pop()
                match token:
                    case "+":
                        stack.append(left + right)
                    case "-":
                        stack.append(left - right)
                    case "*":
                        stack.append(left * right)
                    case "/":
                        stack.append(int(left / right))
            else:
                stack.append(int(token))
        return stack[0]
