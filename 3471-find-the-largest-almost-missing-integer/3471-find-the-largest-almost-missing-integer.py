from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 1:
            cnt = Counter(nums)
            ans = -1
            for x, f in cnt.items():
                if f == 1:
                    ans = max(ans, x)
            return ans
        if k == n:
            return max(nums)
        ans = -1
        if nums.count(nums[0]) == 1:
            ans = max(ans, nums[0])
        if nums.count(nums[-1]) == 1:
            ans = max(ans, nums[-1])
        return ans