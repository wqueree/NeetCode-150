from typing import Set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occured: Set[str] = set()
        start: int = 0
        finish: int = 0
        longest: int = 0
        while finish < len(s):
            if s[finish] in occured:
                occured.remove(s[start])
                start += 1
            else:
                longest = max(longest, finish - start + 1)
                occured.add(s[finish])
                finish += 1
        return longest
