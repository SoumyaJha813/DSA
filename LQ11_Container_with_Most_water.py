class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 
        j = len(height)-1
        max_water = 0
        curr_water = 0
        for x in range(len(height)):
            curr_water = (min(height[i], height[j]))*abs(j-i)
            #print(f"height[i]:{height[i]}, height[j]:{height[j]}, current water: {curr_water}")
            if curr_water > max_water:
                max_water = curr_water
            if height[i]<height[j]:
                i+=1
            elif height[i]>height[j]:
                j-=1
            elif height[i]==height[j]:
                i+=1
                j-=1
        #print(max_water)
        return max_water
