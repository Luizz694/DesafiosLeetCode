#vou modificar algumas coisas da questão do LeetCode
pico = -1
#mount1 = [0,1,2,4,5,4,3,2,1,0] #valida!!
#mount1 = [2,1] #inválida
mount1 = [0,3,2,1] #valida
resultado = True
i = 0
inicio = mount1[0]

for k in range(len(mount1)):
    if(mount1[k] > pico):
        pico = mount1[k]

if(inicio == 0):
    for i in range(len(mount1)-1):
        if (mount1[i] == pico):
            if(mount1[i] > mount1[i+1]):
                resultado = True
            else:
                resultado = False
                break
            pico = mount1[i+1] #a lógica do pico não ser mais pico, é pq eu queria um usa-lo como um "ponteiro" ou "seta" 
        else:
            if(mount1[i+1] < mount1[i] and pico < mount1[i] or pico < mount1[i+1]):
                resultado = False
                break
else:
    resultado = False

print(resultado)