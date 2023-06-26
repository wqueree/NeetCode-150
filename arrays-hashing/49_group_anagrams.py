from collections import defaultdict
from typing import Dict, List, Tuple

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: Dict[Tuple[int], List[str]] = defaultdict(list)
        for word in strs:
            counts: List[int] = [0 for _ in range(26)]
            for char in word:
                counts[ord(char) - ord('a')] += 1
            groups[tuple(counts)].append(word)
        return groups.values()
