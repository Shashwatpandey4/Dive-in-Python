nums = [-2,1,-3,4,-1,2,1,-5,4]
answer = nums[0]
currSum = 0
for n in nums:
    if currSum < 0 :
        currSum = 0
    currSum += n
    answer = max(answer,currSum)


print(answer)