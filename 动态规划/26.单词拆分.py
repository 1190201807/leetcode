# class Solution:
# def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#     dp = [False] * (len(s) + 1)
#     dp[0] = True
#     for j in range(1, (len(s) + 1)):
#         for i in range(len(wordDict)):
#             word = wordDict[i]
#             if s[0:j].endswith(word):
#                 dp[j] = dp[j - len(word)] or dp[j]
#     print(dp)
#     return dp[len(s)]
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.trace(s, wordDict, 0)

    def trace(self, s, wordDict, startIndex):
        if startIndex >= len(s):
            return True

        for i in range(startIndex, len(s)):
            if s[startIndex : i + 1] in wordDict:
                if self.trace(s, wordDict, i + 1):
                    return True
        return False
