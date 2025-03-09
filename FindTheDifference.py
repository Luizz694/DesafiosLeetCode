import random
import string


texto = str(input("Digite uma palavra: "))
texto_embaralhado = ''.join(random.sample(texto, len(texto))) + random.choice(string.ascii_letters)

print(texto)
print(texto_embaralhado)

for char in texto_embaralhado:
    if char in texto:
        print("Tem", char)
    else:
        print("Não tem", char)