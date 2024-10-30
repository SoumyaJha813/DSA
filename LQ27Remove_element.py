class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l1 = len(nums)
        nums2 = [None]*l1
        l2 =  len(nums2)
        i = 0
        j = 0
        k = 0
        while i < l1 and j < l2:
            if nums[i] == val:
                i += 1
                continue

            elif nums[i] != val:
                nums2[j] = nums[i]
                j += 1
                k += 1
            i += 1
        for z in range(l2):
            nums[z] = nums2[z]
            z += 1 
        return k       
        
