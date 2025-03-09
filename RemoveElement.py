x = 2
array = [0,1,2,2,3,0,4,2]
i = 0

for j in range(len(array)):
    if array[i] == x:
        array.pop(i)

    else:
        i=i+1


print(len(array), array)