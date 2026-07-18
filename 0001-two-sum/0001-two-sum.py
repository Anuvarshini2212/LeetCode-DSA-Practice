class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         hashMap={}
         for i,val in enumerate(nums):
            complement=target-val
            if complement in hashMap:
                return [hashMap[complement],i]
            hashMap[val]=i