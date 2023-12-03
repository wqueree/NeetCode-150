from functools import cache
from typing import List, Tuple


class Solution:


    @cache
    def wordBreakCache(self, s: str, wordEnd: int, wordDict: Tuple[str]) -> List[List[str]]:
        allBreaks: List[List[str]] = list()
        if wordEnd < 0:
            allBreaks.append(list())
            return allBreaks
        for word in wordDict:
            wordStart: int = wordEnd - len(word) + 1
            prefixBreaks: List[List[str]] = self.wordBreakCache(s, wordStart - 1, wordDict)
            if wordStart >= 0 and s[wordStart : wordEnd + 1] == word:
                for prefixBreak in prefixBreaks:
                    allBreaks.append(prefixBreak + [word])
        return allBreaks


    def wordBreakMemo(self, s: str, wordEnd: int, wordDict: List[str], memo: List[List[List[str]]]) -> List[List[str]]:
        allBreaks: List[List[str]] = list()
        if wordEnd < 0:
            allBreaks.append(list())
            return allBreaks
        if memo[wordEnd] is not None:
            return memo[wordEnd]
        for word in wordDict:
            wordStart: int = wordEnd - len(word) + 1
            prefixBreaks: List[List[str]] = self.wordBreakMemo(s, wordStart - 1, wordDict, memo)
            if wordStart >= 0 and s[wordStart : wordEnd + 1] == word:
                for prefixBreak in prefixBreaks:
                    allBreaks.append(prefixBreak + [word])
        memo[wordEnd] = allBreaks
        return allBreaks


    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # functools
        return [" ".join(sentence) for sentence in self.wordBreakCache(s, len(s) - 1, tuple(wordDict))]

        # memoization
        memo: List[List[str]] = [None for _ in range(len(s))]
        return [" ".join(sentence) for sentence in self.wordBreakMemo(s, len(s) - 1, wordDict, memo)]
