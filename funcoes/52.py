### DEFINIÇÃO DE VARIÁVEIS ###
z = [2,1,4,3,4]


### FUNÇÕES ###
def bem_vindo():
    print("Bem vindo! Este programa tem por objetivo ler uma lista e contar a quantidade de vezes que um elemento se repete.")

def contar():
    # count conta quantas vezes o elemento se repete na lista
    contagem = z.count (4)
    print(contagem)

def ordenar_crescente():
    z.sort() #organizou em ordem crescente

def inverter_ordem():
    #reverse inverte a ordem dos elementos de uma lista
    z.reverse() #inverteu


### PROGRAMA PRINCIPAL ###
bem_vindo()
contar()
print(z)
ordenar_crescente()
print(z)
inverter_ordem()
print(z)