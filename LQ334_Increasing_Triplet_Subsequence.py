class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        i = 0 
        j = i+1
        k = j+1
        found = False
        for i in range(len(nums)-2):
            if nums[i]<nums[j]<nums[k]:
                found = True
            else:
                found = False
            i+=1
            j+=1
            k+=1
        '''
        found = False
        seq = 1
        min_num = nums[0]
        max_seq = -sys.maxsize - 1   #medium array - arr[j]
        store_min = min_num #min number - arr[i]
        #max arr - nums[i]
        if len(nums)<3:
            return False
        for i in range(1, len(nums)):
            if nums[i] == min_num:
                continue
            elif nums[i]<min_num:
                min_num = nums[i]
                continue
            elif nums[i]<max_seq:
                max_seq = nums[i]
                store_min = min_num
            elif nums[i]> max_seq:
                if seq ==1:
                    store_min = min_num
                seq+=1
                if seq ==3:
                    found = True
                max_seq = nums[i]
        return found

        
