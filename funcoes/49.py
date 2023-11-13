### FUNÇÕES ###
def bem_vindo():
    print("Bem vindo! Este programa tem por objetivo criar uma lista selecionando apenas os números pares de 0 a 99.")

def nova_lista():
    #if numero %2 ==0 se número divido por 2 é igual a zero
    nova_lista= [ numero for numero in range (100) if numero %2 == 0]
    print(nova_lista)


### PROGRAMA PRINCIPAL ###
bem_vindo()
nova_lista()
