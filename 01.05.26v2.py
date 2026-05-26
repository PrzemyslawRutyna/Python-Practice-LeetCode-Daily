from typing import List
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        ans = -2147483648
        foo = 0
        for i, elem in enumerate(nums):
            foo += i * elem
        foo = 0
        return max(ans, foo)
fooo = Solution()
nums = [4,3,2,6]
print(fooo.maxRotateFunction(nums))
