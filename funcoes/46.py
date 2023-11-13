### DEFINIÇÃO DE VARIÁVEIS ###
lista =[]


### FUNÇÕES ###
def bem_vindo():
    print("Bem vindo! Este programa tem por objetivo criar uma lista e apresentar valores desta lista de forma 'fatiada'.")

def criar_lista():
    for x in range(10):
        lista.append(x)

def imprimir_lista_e_fatias():
    print(lista)
    #Fatias de listas
    print(lista[1:2])
    print(lista[2:5])
    print(lista[5:])
    print(lista[:5])
    print(lista[:])


### PROGRAMA PRINCIPAL ###
bem_vindo()
criar_lista()
imprimir_lista_e_fatias()
lista2=lista[4:8]
print(lista2)
