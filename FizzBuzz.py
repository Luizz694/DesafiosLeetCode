n = int(input("Digite um número: "))
lista = []
i = 1

for _ in range(n):
    if i % 3 == 0:
        if i % 5 ==0:
            lista.append("FizzBuzz")
        else:
            if i % 3 == 0:
                lista.append("Fizz")

    elif i % 5 == 0:
        lista.append("Buzz")

    else:
        lista.append(i)
    
    i = i+1

print(lista)
