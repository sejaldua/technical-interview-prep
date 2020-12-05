class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        total_water = 0
        left_max = [0 for _ in range(len(height))]
        right_max = [0 for _ in range(len(height))]
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(height[i], left_max[i-1])
        right_max[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, 0, -1):
            right_max[i] = max(height[i], right_max[i+1])
        for i in range(1, len(height)):
            total_water += min(left_max[i], right_max[i]) - height[i]
            
        return total_water
