class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_freq = {}
        ran_freq = {}
        for _ in magazine:
            if _ in mag_freq:
                mag_freq[_] += 1
            else:
                mag_freq[_] = 1
        print(mag_freq)
        for x in ransomNote:
            if x in ran_freq:
                ran_freq[x] += 1
            else:
                ran_freq[x] = 1
        print(ran_freq)
        count = 0
        for key in ran_freq:
            if key not in mag_freq or mag_freq[key] < ran_freq[key]:
                return False
        return True
