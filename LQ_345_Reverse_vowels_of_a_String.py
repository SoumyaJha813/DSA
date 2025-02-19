class Solution:
    def reverseVowels(self, s: str) -> str:
        vol = ''
        vow = 'AEIOUaeiou'
        for i in s:
            if i in vow:
                vol+=i
        #print("vowels in string: ",vol)
        rev_vol = vol[::-1]
        #print("reverse vowels: ",rev_vol)
        rev_s = s[::-1]
        new_str = ''
        count1 = 0
        count2 = 0
        for i in s:
            if i in vow:
                new_str += rev_vol[count1]
                count1 +=1
                count2+=1
                #print("new string after adding rev_vol: ", new_str)
            else:
                new_str += s[count2]
                count2 +=1
                #print("new string after adding s: ", new_str)
        #print("output: ",new_str)
        return new_str


        
