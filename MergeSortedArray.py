nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
arm = 0
nums3 = []

if(m==n):
    for i in range(m):
        nums3.append(nums1[i])
        nums3.append(nums2[i])

else:
    for i in range(m):
        nums3.append(nums1[i])

    for j in range(n):
        nums3.append(nums2[j])
    

for i in range(len(nums3)-1):
    if(nums3[i] > nums3[i+1]):
        arm = nums3[i]
        nums3[i] = nums3[i+1]
        nums3[i+1] = arm

print(nums3)