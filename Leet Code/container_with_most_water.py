'''
https://leetcode.com/problems/container-with-most-water/
'''

'''
problem link = https://leetcode.com/problems/container-with-most-water/submissions/
'''

def maxArea(self, height: List[int]) -> int:
        ans, i, j = 0, 0, len(height)-1
        while (i < j):
            if height[i] <= height[j]:
                res = height[i] * (j - i)
                i += 1
            else:
                res = height[j] * (j - i)
                j -= 1
            if res > ans: ans = res
        return ans


