class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False   
        for k in range(len(s)):
            if goal == s[k:] + s[:k]:
                return True
        return False
s = "abcde"
goal = "abced"
foo = Solution()
print(foo.rotateString(s, goal))
            

    