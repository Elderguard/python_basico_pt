### DEFINIÇÃO DE VARIÁVEIS ###
lista = [1,2,3,4,5]


### FUNÇÕES ###
def bem_vindo():
    print("Bem vindo! Este programa tem por observar uma lista, imprimi-la, imprimir o número de elementos na lista, adicionar e remover elementos.")

def imprimir_sobre_lista():
    print(lista)
    print(len(lista)) #imprime o tamanho (nro elementos) da lista

def adicionar_itens():
    lista.insert(2,22) #insere na posição 2 o elemento 22
    lista.append(33) #insere o 33 no final da lista

def deletar_itens():
    #remove elemento na posição 4 da lista

    del lista[4]

def remove_valor():
    #remove o elemento 22 da lista
    lista.remove(22)


### PROGRAMA PRINCIPAL ###
bem_vindo()
imprimir_sobre_lista()
adicionar_itens()
imprimir_sobre_lista()
deletar_itens()
imprimir_sobre_lista()
remove_valor()
imprimir_sobre_lista()
