#Listas - calcular intersecção de conjuntos

lista1 = [1,2,3,4,9,6]
lista2 = [3,4,5,6,7,8]

uniao = []

for nro in lista1:
    uniao.append(nro)
for nro in lista2:
    if nro not in lista1:
        uniao.append(nro)


print(uniao)