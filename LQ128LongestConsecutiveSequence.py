class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset =  set(nums)
        maxseq = 0
        if not nums:
            return 0
        for num in numset:
            if num-1 not in numset:
                current_num  = num
                seq = 1
                while current_num+1 in numset:
                    current_num += 1
                    seq += 1
                maxseq = max(maxseq, seq)
        return maxseq
