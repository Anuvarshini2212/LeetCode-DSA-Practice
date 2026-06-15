class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         temp={}
         for i in range(len(nums)):
            need = target - nums[i]
            if need in temp:
                return [temp[need], i]
            temp[nums[i]] = i