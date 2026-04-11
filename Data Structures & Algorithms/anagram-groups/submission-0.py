class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}
        n = len(strs)

        for i in range(n):
            temp = "".join(sorted(strs[i]))
            if temp in grp:
                grp[temp].append(strs[i])
            else:
                grp[temp] = [strs[i]]

        return list(grp.values())