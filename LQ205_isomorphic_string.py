class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        i=0
        j=0
        while i < len(s) and j < len(t):
            s_map[s[i]] = i
            t_map[t[j]] = j
            i+=1
            j+=1
        s_list = list(s_map.values())
        t_list = list(t_map.values())
        if s_list == t_list:
            return True
        else:
            return False
