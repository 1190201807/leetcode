from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i = 0
        j = 0
        mapP = Counter(p)
        # for ch in p:
        #     if ch in mapP:
        #         mapP[ch] +=1
        #     else:
        #         mapP[ch] = 1

        windows = {}
        l = 0
        res = []
        for index, ch in enumerate(s):
            if ch not in mapP:
                windows.clear()
                l = index + 1
                print(l)
                continue
            windows[ch] = windows.get(ch, 0) + 1
            print(windows)
            while windows[ch] > mapP[ch]:
                windows[s[l]] -= 1
                l += 1
            if (index - l + 1) == len(p):
                res.append(l)
        return res
