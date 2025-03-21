nums = [1,3,5,6]
target = 3
i = 0

while i < len(nums):
    if nums[i] == target:
        arm = i
        break

    if  i == len(nums)-1:
        for k in range(len(nums)):
            if nums[k] > target:
                arm = k
                break
            else:
                arm = k
    i=i+1

print(arm)
#código está em O(n) :/

