class Solution:
    def rotatedDigits(self, n: int) -> int:
        invalid = {'3', '4', '7'}
        changing = {'2', '5', '6', '9'}
        ans = 0
        for i in range(1, n + 1):
            s = str(i)
            if not (set(s) & invalid) and (set(s) & changing):
                ans += 1
        return ans

print(Solution().rotatedDigits(10))
print(Solution().rotatedDigits(20))
