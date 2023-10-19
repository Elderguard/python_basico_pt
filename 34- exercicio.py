lista=[6,20,2,14,7,17]

#somar os valores
soma = 0
for x in lista:
    print('x = ', x)
    print('soma = ', soma)
    soma = soma + x
    print('soma após laço = ', soma)
print("Soma = ", soma)

#media dos valores
media = soma/6
print("media = ", media)

#maior valor
maior = 0
menor = 10000
for x in lista:
    if x>maior:
        maior=x
#menor valor
    if x<menor:
        menor=x

print("maior = ", maior)
print("menor = ", menor)