from typing import List
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         def bin_search(left, right):
#             if left > right:
#                 return -1 
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 return mid
#             if nums[left] <= nums[mid]:
#                 if nums[left] <= target < nums[mid]:
#                     return bin_search(left, mid - 1)
#                 else:
#                     return bin_search(mid + 1, right)
#             else:
#                 if nums[mid] < target <= nums[right]:
#                     return bin_search(mid + 1, right)
#                 else:
#                     return bin_search(left, mid - 1)
#         return bin_search(0, len(nums) - 1)
# ITERATIVE SOLUTION      
class Solution:
     def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1