class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        llist = {}
        i = 0
        while i < len(nums):
            if nums[i] in llist:
                return True
            else:
                llist[nums[i]] = i
            i+=1
        return False
