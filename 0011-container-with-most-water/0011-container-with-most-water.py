class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_a=0
        while left<right:
            w=right-left
            a=min(height[left],height[right])*w
            max_a=max(max_a,a)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_a