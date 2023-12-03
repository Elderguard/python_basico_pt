### DEFINIÇÃO DE VARIÁVEIS ###
lista = [0,1,2,3,4,5]

### FUNÇÕES ###
def bem_vindo():
    print("Bem vindo! Este programa tem por objetivo ler uma lista e criar uma nova lista com os elementos tendo o dobro do valor da lista base.")

def nova_lista():
    nova_lista = [numero * 2 for numero in lista]
    print(nova_lista)


### PROGRAMA PRINCIPAL ###
bem_vindo()
nova_lista()
