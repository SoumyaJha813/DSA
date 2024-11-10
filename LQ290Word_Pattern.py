class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_m = {}
        i = 0
        j = 0
        s1 = s.split(' ')
        print(s1)
        print("len pattern: ", len(pattern))
        print("len s: ", len(s1))
        if len(s1)!=len(pattern):
            return False
        while i < len(pattern) and j < len(s1):
            if pattern[i] in hash_m:
                val = hash_m.get(pattern[i])
                if s1[j] != val:
                    return False
            else:
                hash_m[pattern[i]] = s1[j]
            i+=1
            j+=1
        print(hash_m)
        print(hash_m.values())
        for x in s1:
            if x not in hash_m.values():
                return False
                print(hash_m.values())
        l1 = hash_m.values()
        freq_l1 = {}
        for _ in l1:
            if _ in freq_l1:
                freq_l1[_] += 1
                return False
            else:
                freq_l1[_] = 1
        
        return True
