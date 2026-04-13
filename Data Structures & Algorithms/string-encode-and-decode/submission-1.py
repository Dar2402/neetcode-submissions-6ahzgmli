class Solution:

    def transform(self, s, n, to_do="en"):
        temp = ""
        if to_do == "en":
            temp = str(n) + "#"
            
            for i in s:
                temp = temp + chr(ord(i) + n)
            
            return temp
        else:
            for i in s:
                temp = temp + chr(ord(i) - n)
            return temp

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            n = len(i)
            res = res + self.transform(i, n)
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res2 = []
        for i in range(len(s)):
            if s[i].isdigit() and i < len(s) - 1:
                if s[i + 1] != "#":
                    continue
                res2.append(self.transform(s[i + 2: i + int(s[i]) + 2], int(s[i]), "de"))
        return res2
