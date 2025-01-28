class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-1):
            print("nums (0, i): ",nums[0:i+1])
            sum_left = sum(nums[0:i+1])
            print("sum_left: ", sum_left)
            print("nums (i+1, n-1): ", nums[i+1:len(nums)])
            sum_right = sum(nums[i+1:len(nums)])
            print("sum_right: ", sum_right)
            print("sum_left - sum_right: ",sum_left-sum_right)
            if (sum_left - sum_right) %2 == 0:
                count += 1
            print(count) 
        return count
        
