nums = [-3,-1,-1]
ans = max(nums)
currMin, currMax = 1,1

for n in nums:
    tmp = currMax*n
    currMax = max(currMax*n, currMin*n,n)
    currMin = min(tmp,currMin*n,n)
    ans = max(ans,currMax)

print(ans)
