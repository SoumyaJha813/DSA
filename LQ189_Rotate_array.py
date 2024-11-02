class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp  = []
        k = k % len(nums)
        temp = nums[-k:]
        temp += nums[:-k]
        for z in range(len(nums)):
            nums[z] = temp[z]
        print(nums)
