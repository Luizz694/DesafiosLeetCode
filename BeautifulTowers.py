heights = [1,1,3,5,3,4,1,1]
pico = 0
PointAnt = 0
PointPost = 0
soma = 0

for i in range(len(heights)):
    if(heights[i] > pico):
        pico = heights[i]

if(heights[0] == pico):
    PointPost = heights[1]
    Validador = False
else:
    for i in range(len(heights)):
        if(heights[i] == pico):
            PointAnt = heights[i-1]
            PointPost = heights[i+1]
            Validador = True

if (Validador == True):
    for k in range(len(heights)-1):
            if(heights[k] == pico):
                if(heights[k+1] > PointPost):
                    arm = heights[k+1]-PointPost
                    heights[k+1] = heights[k+1]-arm
                    if(heights[k+1] <= 1):
                        heights[k+1] = 1

                if(heights[k+1] < PointPost):
                    arm = PointPost-heights[k+1]
                    heights[k+1] = heights[k+1]-arm
                    if(heights[k+1] <= 1):
                        heights[k+1] = 1

                pico = heights[k+1]
            else:
                if(heights[k] > PointAnt):
                    arm = heights[k]-PointAnt
                    heights[k] = heights[k]-arm
                    if(heights[k] <= 1):
                        heights[k] = 1

                if(heights[k] < PointAnt):
                    arm = PointAnt-heights[k]
                    heights[k] = heights[k]-arm
                    if(heights[k] <= 1):
                        heights[k] = 1
    
    for j in range(len(heights)):
        soma = soma + heights[j]

if (Validador == False):
    for k in range(len(heights)-1):
            if(heights[k] == pico and PointPost > pico):
                PointPost = pico
                if(heights[k+1] >= PointPost):
                    arm = heights[k+1]-PointPost
                    heights[k+1] = heights[k+1]-arm
                    if(heights[k+1] <= 1):
                        heights[k+1] = 1
                else:
                    arm = PointPost-heights[k+1]
                    heights[k+1] = heights[k+1]-arm
                    if(heights[k+1] <= 1):
                        heights[k+1] = 1

                pico = heights[k+1]
            else:
                if(heights[k] == pico):
                    if(heights[k+1] > PointPost):
                        arm = heights[k+1]-PointPost
                        heights[k+1] = heights[k+1]-arm
                        if(heights[k+1] <= 1):
                            heights[k+1] = 1

                    if(heights[k+1] < PointPost):
                        arm = PointPost-heights[k+1]
                        heights[k+1] = heights[k+1]-arm
                        if(heights[k+1] <= 1):
                            heights[k+1] = 1

                pico = heights[k+1]

    for j in range(len(heights)):
        soma = soma + heights[j]

print(heights)
print(soma)
#Quantos laços meu Deus!!