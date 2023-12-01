from functools import cache
from typing import List, Tuple


class Solution:


    @cache
    def wordBreakCache(self, s: str, wordEnd: int, wordDict: Tuple[str]) -> bool:
        if wordEnd < 0:
            return True
        for word in wordDict:
            wordStart: int = wordEnd - len(word) + 1
            if wordStart >= 0 and s[wordStart : wordEnd + 1] == word and self.wordBreakCache(s, wordStart - 1, wordDict):
                return True
        return False


    def wordBreakMemo(self, s: str, wordEnd: int, wordDict: List[str], memo: List[int]) -> bool:
        if wordEnd < 0:
            return True
        if memo[wordEnd] != -1:
            return memo[wordEnd] == 1
        for word in wordDict:
            wordStart: int = wordEnd - len(word) + 1
            if wordStart >= 0 and s[wordStart : wordEnd + 1] == word and self.wordBreakMemo(s, wordStart - 1, wordDict, memo):
                memo[wordEnd] = 1
                return True
        memo[wordEnd] = 0
        return False


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # functools
        return self.wordBreakCache(s, len(s) - 1, tuple(wordDict)) 

        # memoization
        memo: List[int] = [-1 for _ in range(len(s))]
        return self.wordBreakMemo(s, len(s) - 1, wordDict, memo)
