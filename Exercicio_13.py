import math

contar_pares = 0
contar_impares = 0

for i in range(10):
    entrada = input('Digite seu numero : ')

    numero = int(entrada)
    if numero % 2 == 0:
        contar_pares += 1
    else:
        contar_impares += 1
print('Quantidade pares:', contar_pares)
print('Quantidade impares:', contar_impares)