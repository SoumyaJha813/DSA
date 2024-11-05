class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l1 = len(nums)
        i = 0
        maxReach = 0
        while i < l1:
            if i > maxReach: #you cannot move further as you don't have fuel(no - jump left)
                return False
            maxReach = max(maxReach, i+ nums[i]) #Accumulate the max jump you can do from particular index
            if i >= (l1-1): #Reached at the end of array- completed the distance
                return True
            i += 1
