nums = [-1,0,1,2,-1,-4,0,1]

for i in range(len(nums)-2):
    for j in range(len(nums)-2):
        if(nums[i] + nums[j+1] + nums[j+2] == 0):
            print("Valores:", nums[i], nums[j+1], nums[j+2])


    

