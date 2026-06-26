class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        original = x
        digit_sum = 0
        while x > 0:
            digit_sum += x % 10
            x //= 10
        if original % digit_sum == 0:
            return digit_sum
        return -1