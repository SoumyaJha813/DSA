class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        llist = {}
        bool1 = False
        while i < len(nums):
            if nums[i] in llist and abs(i - llist[nums[i]])<=k:
                return True
            else:
                llist[nums[i]] = i
            i+=1
        return False
                
