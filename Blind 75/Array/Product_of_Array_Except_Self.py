nums = [1,2,3,4]

'''
for i,n in enumerate(nums):
    copy = nums.copy()
    print(copy)
    copy.remove(copy[i])
    print(copy)
    print(nums)
    res = 1
    for c in copy:
        res = res*c
    answer.append(res)
    print(res)
    print(answer)
'''
ans = [1]*len(nums)
for i in range(len(nums)-1):
    i+=1
    print(nums[i])
    ans[i] = ans[i-1]*nums[i-1]
print(ans)
temp=1
for i in reversed(range(len(nums))):
    print(nums[i])
    ans[i] = ans[i]*temp
    temp*=nums[i]
print(ans)