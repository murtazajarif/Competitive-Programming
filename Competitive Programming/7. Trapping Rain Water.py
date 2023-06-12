class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height == []:
            return 0
        max_right = [-1]*len(height)
        for i in range(len(height)-1, -1, -1):
            max_right[i] = max(height[i], max_right[i+1]) if i < len(height)-1 else height[i]
        water_trap, max_left = 0, height[0]
        for i in range(1, len(height)-1):
            h_left, h_right = max_left, max_right[i+1]
            if h_left > height[i] and h_right > height[i]:
                water_trap += min(h_left,h_right) - height[i]
            max_left = max(max_left, height[i])
        return water_trap