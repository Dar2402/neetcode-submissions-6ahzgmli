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
        for i, s in enumerate(strs):
            strs[i] = '{:03d}'.format(len(s)) + s
        return "".join(strs)


    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            a = i + 3
            b = int(s[i:a]) + a
            strs.append(s[a:b])
            i = b
        return strs
