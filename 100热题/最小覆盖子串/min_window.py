"""
LeetCode 76. 最小覆盖子串（Minimum Window Substring）
https://leetcode.cn/problems/minimum-window-substring/

返回 s 中覆盖 t 全部字符（含重复）的最短窗口子串；不存在返回 ""。

核心思路：滑动窗口 + 字符计数
时间复杂度：O(m + n)   空间复杂度：O(C)，C 为字符集大小
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)        # t 中每个字符需要的数量（含重复，如 t="aa" 则 need['a']=2）
        window = {}              # 当前窗口内各字符的计数
        required = len(need)     # 需要凑齐的字符"种类"数
        formed = 0               # 已凑齐的种类数
        ans_l, ans_len = 0, float("inf")

        l = 0
        for r, ch in enumerate(s):          # ① R 一步步扩张
            window[ch] = window.get(ch, 0) + 1
            # 某字符数量"恰好"达到需求时 formed+1（之后超出的不重复计数）
            if ch in need and window[ch] == need[ch]:
                formed += 1

            # ② 一旦覆盖，就收缩 L 直到刚好不覆盖，期间不断记录更短的答案
            while formed == required:
                if r - l + 1 < ans_len:     # 先记录，再收缩
                    ans_l, ans_len = l, r - l + 1
                out = s[l]
                window[out] -= 1
                # 移出的字符导致某种类数量跌破需求 → 不再覆盖
                if out in need and window[out] < need[out]:
                    formed -= 1
                l += 1

        return "" if ans_len == float("inf") else s[ans_l: ans_l + ans_len]


if __name__ == "__main__":
    sol = Solution()
    assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert sol.minWindow("a", "a") == "a"
    assert sol.minWindow("a", "aa") == ""
    assert sol.minWindow("ab", "b") == "b"
    print("所有测试通过 ✅")
