# from typing import List
# from collections import defaultdict
# class Solution:
#     def longestBalanced(self, nums: List[int]) -> int:
#         counts = defaultdict(int)
#         left = 0 
#         best = 0
#         distinct_odd = 0
#         distinct_even = 0
#         n = len(nums)

#         for right in range(n):
#             num = nums[right]
#             counts[num] += 1
#             if counts[num] == 1:
#                 if num % 2 == 0:
#                     distinct_even += 1
#                 else:
#                     distinct_odd += 1

#             while distinct_odd != distinct_even:
#                 num = nums[left]
#                 counts[num] -= 1
#                 if counts[num] == 0:
#                     if num % 2 == 0:
#                         distinct_even -= 1
#                     else:
#                         distinct_odd -= 1
#                 left += 1
#             best = max(best, right - left + 1)
#         return best 
# SLIDING WINDOW SOLUTION - DOESNT EVEN WORK
from typing import List
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        best = 0
        n = len(nums)

        for i in range(n):
            odds = set()
            evens = set()
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    evens.add(nums[j])
                else:
                    odds.add(nums[j])
                if len(odds) == len(evens):
                    best = max(best, j - i + 1)
        return best