class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        ers = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                five += 1
            elif bills[i] == 10:
                five -= 1
                ten += 1
            else:
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 2
            if five < 0 or ten < 0 or ers < 0:
                return False
        return True
