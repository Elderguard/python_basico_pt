#Funções
def bemVindo():
    print("Bem vindo! Este programa tem por objetivo receber valores numéricos informados pelo usuário para formar uma lista, somar e informar o tamanho da lista.")

def coletarValores():
    global lista
    lista = []
    while True:
        entrada = input("Informe o valor que quer adicionar ou digite s para sair.")
        if entrada == 's':
            print("Foi dado o comando de sair.")
            print(f"A lista tem {len(lista)} valores informados")
            break
        else:
            lista.append(float(entrada))
        print(f"A lista é: {lista}")

def somar():
    global soma
    soma = 0
    for x in lista:
        soma = soma + x     
    print('soma = ', soma)

def calculaMedia():
    media = soma/(len(lista))
    print("media = ", media)



#Programa Principal
bemVindo()
coletarValores()
somar()
calculaMedia()
