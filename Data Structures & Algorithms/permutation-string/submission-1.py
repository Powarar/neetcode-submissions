from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Counter = Counter(s1)
        curCounter = Counter()

        for i in range(len(s1)):
            curCounter[s2[i]] += 1
        if curCounter == s1Counter:
            return True

        for i in range(len(s1), len(s2)):
            curCounter[s2[i - len(s1)]] -=1
            curCounter[s2[i]] +=1

            if curCounter == s1Counter:
                return True
        return False