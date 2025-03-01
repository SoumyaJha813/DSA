class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        new_nums = [0]*len(nums)
        i = 0
        j = len(nums)-1
        for x in nums:
            if x == 0:
                new_nums[j]=x
                j-=1
            else:
                new_nums[i] = x
                i+=1
        nums = new_nums
        print("nums: ", nums)
        print("new_nums", new_nums)
        return nums
        '''
        count =0
        for x in range(len(nums)):
            if nums[x] != 0:
                nums[count]=nums[x]
                count +=1
        while count < len(nums):
            nums[count] = 0
            count +=1
        print("nums: ", nums)
        return nums


