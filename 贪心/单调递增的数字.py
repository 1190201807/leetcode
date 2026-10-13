class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = str(n)
        flag = -1
        for i in range(len(s) - 1, 0, -1):
            if s[i] < s[i - 1]:
                flag = i
                s = s[: i - 1] + str(int(s[i - 1]) - 1) + "9" + s[i + 1 :]
        for i in range(flag, len(s)):
            if flag != -1:
                s = s[:i] + "9" + s[i + 1 :]
        return int(s)
