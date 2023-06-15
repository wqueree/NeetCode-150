from collections import defaultdict
from typing import Dict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s: Dict[str, int] = defaultdict(int)
        count_t: Dict[str, int] = defaultdict(int)
        for i in range(len(s)):
            count_s[s[i]] += 1
            count_t[t[i]] += 1
        return count_s == count_t
