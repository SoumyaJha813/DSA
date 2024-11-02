class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_nums= {}
        for i in nums:
            if i in freq_nums:
                freq_nums[i] += 1
            else:
                freq_nums[i] = 1
        max_freq = max(freq_nums, key = freq_nums.get)
            
        return max_freq
