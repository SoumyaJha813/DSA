class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        llist = {}
        for x in range(len(nums)):
            y = target - nums[x]
            if y in llist:
                return llist[y],x
            llist[nums[x]] = x
        
                
