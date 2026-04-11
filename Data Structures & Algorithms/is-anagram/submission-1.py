class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l_s = len(s)
        l_t = len(t)
        count = {}

        if l_s != l_t:
            return False

        for c in s:
            count[c] = count.get(c, 0) + 1
        
        for c in t:
            count[c] = count.get(c, 0) - 1

            if count[c] < 0:
                return False
        return True

        # for c in s:
        #     if s.count(c) != t.count(c):
        #         return False
        #     continue
        # return True
        