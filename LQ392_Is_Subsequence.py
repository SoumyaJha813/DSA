class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0 
        for x in range(len(t)):
            if s == "":
                return True
            elif i<= (len(s)-1) and s[i] == t[j]:
                print("Common element: s[i]:", s[i], "t[j]: ", t[j])
                i+=1
                j+=1
            elif i<=(len(s)-1) and s[i] != t[j]:
                j+=1
        if i == len(s):
            return True
        else:
            return False
