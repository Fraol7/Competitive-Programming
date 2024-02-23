class Solution:
    def trap(self, height: List[int]) -> int:
        stack = height[0]
        rain = 0
        left = 0
        while left < len(height)-1:
            right = left + 1
            temp = 0
            while right < len(height) and stack > height[right]:
                temp += height[right]
                right += 1
            if right == len(height):
                height[left] -= 1
                stack -= 1
                continue
            rain += stack*(right-left-1) - temp
            left = right
            stack = height[left]
        return rain

            

