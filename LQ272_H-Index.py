class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ll = []
        ll = sorted(citations, reverse = True)
        print(ll)
        count = 1
        for fn in ll:
            if ll[0] == 0:
                return 0
            if len(ll) == 1:
                return 1
            if fn >= count and count < len(ll) and ll[count] < (count+1):
                return count
            elif fn >= count and count == len(ll) and ll[count-1] >= count:
                return count 
            count += 1
