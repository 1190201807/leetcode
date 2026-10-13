class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        self.trace(digits, "", 0, result)
        return result

    def __init__(self):
        self.letters = [
            "" ,  # 0 
            "",  # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs",  # 7
            "tuv",  # 8
            "wxyz",  # 9
        ]

    def trace(self, digits,path, curDep, result):
        if curDep == len(digits):
            result.append(path[:])
            return
        for i in self.letters[int(digits[curDep])]:
            self.trace(digits, path + i, curDep + 1, result)
