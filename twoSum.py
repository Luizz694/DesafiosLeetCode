lista = [2,7,11,15]
alvo = 26

#O(n)
for i in range (len(lista)):
    if(lista[i] + lista[i+1] == alvo):
        print(i, i+1)
        break
