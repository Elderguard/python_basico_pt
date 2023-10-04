candidato1 = input("Nome do candidato 1:")
nrovotos1 = int(input("Nro de votos do candidato 1: "))

candidato2 = input("Nome do candidato 2:")
nrovotos2 = int(input("Nro de votos do candidato 2: "))

candidato3 = input("Nome do candidato 3:")
nrovotos3 = int(input("Nro de votos do candidato 3: "))

print(nrovotos1)
print(nrovotos2)
print(nrovotos3)
totalvotos = nrovotos1 + nrovotos2 + nrovotos3

print ("Total de votos: ", totalvotos)

frac_votos1 = nrovotos1/totalvotos
frac_votos2 = nrovotos2/totalvotos
frac_votos3 = nrovotos3/totalvotos

porc_votos1 = frac_votos1*100
porc_votos2 = frac_votos2*100
porc_votos3 = frac_votos3*100

print ("Porcentagem de votos 1: %.2f" % porc_votos1, " %")
print ("Porcentagem de votos 2: %.2f" % porc_votos2, " %")
print ("Porcentagem de votos 3: %.2f" % porc_votos3, " %")