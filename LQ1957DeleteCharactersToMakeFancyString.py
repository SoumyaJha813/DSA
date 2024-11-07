class Solution:
    def makeFancyString(self, s: str) -> str:
        s_len = len(s)
        count = 0
        s_cp = ''
        if s_len<=2:
            return s
        else:
            for i in range(s_len):
                if i> 0 and s[i] == s[i-1]:
                    count += 1
                else:
                    count = 1
                if count <=2:
                    s_cp += s[i]
        return s_cp
