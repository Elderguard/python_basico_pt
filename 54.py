#Listas - calcular intersecção de conjuntos

lista1 = [1,2,3,4,9,6]
lista2 = [3,4,5,6,7,8]

interseccao = []

for nro in lista1:
    if nro in lista2:
        interseccao.append(nro)

print(interseccao)