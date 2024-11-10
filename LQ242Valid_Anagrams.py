class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}
        for _ in s:
            if _ in freq_s:
                freq_s[_] += 1
            else:
                freq_s[_] = 1
        for x in t:
            if x in freq_t:
                freq_t[x] += 1
            else:
                freq_t[x] = 1
        print(freq_s.keys())
        print(freq_t.keys())
        if len(s) != len(t):
            return False
        if freq_s.keys() != freq_t.keys():
            return False
        for q in freq_s.keys():
            if q in freq_t.keys() and (freq_s.get(q) == freq_t.get(q)):
                return True
            else:
                return False
