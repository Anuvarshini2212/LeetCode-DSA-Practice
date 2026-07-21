class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        left, right = 1, 1000000

        while left < right:
            mid = (left + right) // 2
            apples = 2 * mid * (mid + 1) * (2 * mid + 1)

            if apples >= neededApples:
                right = mid
            else:
                left = mid + 1

        return 8 * left