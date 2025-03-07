num1 = [3,2,1]
num2 = [2,1] 
numero1 = 0
numero2 = 0
k= 1
j= 1

for i in range(len(num1)):
    numero1 = numero1 + num1[i]*k
    k = k*10

for i in range(len(num2)):
    numero2 = numero2 + num2[i]*j
    j = j*10

vetorSoma = []
soma = numero1+numero2

if len(num1) > len(num2):
    for i in range(len(num1)+1):
        arm = soma // k%10
        if i > 0 or arm != 0: 
            vetorSoma.append(arm)
        k = k//10

    for x in range(len(vetorSoma)-1):
        for i in range(len(vetorSoma)-1):
            if vetorSoma[i] <= vetorSoma[i+1]:
                arm = vetorSoma[i]
                vetorSoma[i] = vetorSoma[i+1]
                vetorSoma[i+1] = arm

if len(num2) > len(num1):
    for i in range(len(num2)+1):
        arm = soma // j%10
        if i > 0 or arm != 0: 
            vetorSoma.append(arm)
        j = j//10

    for x in range(len(vetorSoma)-1):
        for i in range(len(vetorSoma)-1):
            if vetorSoma[i] <= vetorSoma[i+1]:
                arm = vetorSoma[i]
                vetorSoma[i] = vetorSoma[i+1]
                vetorSoma[i+1] = arm




print(numero1)
print(numero2)
print(soma)
print(vetorSoma)
