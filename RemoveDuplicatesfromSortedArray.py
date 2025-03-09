nums = [0,0,1,1,4,4,6,6,6]
i = 0


#desisto por enquanto kkkkkk
for j in range(len(nums)-1):
    if nums[i] == nums[i+1]:
        nums.pop(i)

    elif nums[i] != nums[i+1]:
        i=i+1


print(nums)









        