class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        Max=Min=res=nums[0]
        for i in nums[1:]:
            if i<0:
                Max,Min=Min,Max
            Max=max(i,Max*i) 
            Min=min(i,Min*i)
            res=max(res,Max)
        return res