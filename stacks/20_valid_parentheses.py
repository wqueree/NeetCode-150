from typing import Dict, List

class Solution:
    def isValid(self, s: str) -> bool:
        matches: Dict[str, str] = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack: List[str] = list()
        for c in s:
            if c in matches.values():
                stack.append(c)
            elif stack and matches[c] == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
