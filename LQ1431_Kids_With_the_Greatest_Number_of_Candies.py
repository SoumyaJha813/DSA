class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxc =  max(candies)
        #print(maxc)
        llist = [0]*len(candies)
        count = 0
        for i in candies:
            if i + extraCandies >= maxc:
                llist[count] = True
            else:
                llist[count] =  False
            count += 1
        #print(llist)
        return llist
