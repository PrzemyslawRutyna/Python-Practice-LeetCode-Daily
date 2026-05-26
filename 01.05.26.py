from typing import List
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        f = sum(i * x for i, x in enumerate(nums))
        ans = f
        for k in range(1, n):
            f += total - n * nums[n - k]
            ans = max(ans, f)
        return ans
fooo = Solution()
nums = [4,3,2,6]
print(fooo.maxRotateFunction(nums))
print()