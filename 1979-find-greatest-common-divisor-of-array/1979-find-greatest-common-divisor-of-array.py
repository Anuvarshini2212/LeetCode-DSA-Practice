class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        s=nums[0]
        l=nums[-1]
        while l!=0:
            s,l=l,s%l
        return s