class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = []
        i = j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1

        while i < m:
            nums3.append(nums1[i])
            i += 1
        while j < n:
            nums3.append(nums2[j])
            j += 1

        print(nums3)
        for k in range(m+n):
            nums1[k] = nums3[k]
        return nums1

