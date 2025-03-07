
list = [1,2,3,4]
for i in range(len(list)-1):
    if list[i+1] % 2 == 0:
        arm = list[i]
        list[i] = list[i+1]
        list[i+1] = arm


print(list)
    
