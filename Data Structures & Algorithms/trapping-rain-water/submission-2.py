class Solution:
    def trap(self, height: List[int]) -> int:

        # 1. Find peak's index
        peak = 0
        for i in range(len(height)):
            if height[peak] < height[i]:
                peak = i

        # 2. Loop from start to peak
        left = 0
        right = 1

        save = 0
        trapped = 0
        
        while right <= peak:
            if height[left] <= height[right]:
                trapped += min(height[left], height[right]) * (right - left - 1) - save
                left = right
                right += 1
                save = 0
            
            else:
                save += height[right]
                right += 1

        # 3. Loop from end to peak
        left = len(height) - 2
        right = len(height) - 1

        while peak <= left: 
            if height[left] >= height[right]:
                trapped += min(height[left], height[right]) * (right - left - 1) - save
                right = left
                left -= 1
                save = 0
            
            else:
                save += height[left]
                left -= 1

        return trapped
