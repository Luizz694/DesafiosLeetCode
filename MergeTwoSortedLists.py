lista1 = [1,3,4,67,5]
lista2 = [2,1,7,678,6]
arm = 0

for i in range(len(lista1)):
    lista1.append(lista2[i])

for j in range(len(lista1)-1):
    for i in range(len(lista1)-1):
        if lista1[i] >= lista1[i+1]:
            arm = lista1[i]
            lista1[i] = lista1[i+1]
            lista1[i+1] = arm

print(lista1)






