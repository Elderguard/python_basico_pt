### DEFINIÇÃO DE VARIÁVEIS ###
lista1 = [1,2,3,4,9,6]
lista2 = [3,4,5,6,7,8]

uniao = []

### FUNÇÕES ###
def bem_vindo():
    print("Bem vindo! Este programa tem por objetivo ler duas listas e criar uma união dos elementos em outra lista.")

def encontrar_uniao():
    for nro in lista1:
        uniao.append(nro)
    for nro in lista2:
        if nro not in lista1:
            uniao.append(nro)


    print(uniao)

### PROGRAMA PRINCIPAL ###
bem_vindo()
encontrar_uniao()
