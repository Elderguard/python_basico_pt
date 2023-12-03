#Funções
def bemVindo():
    print("Bem vindo! Este programa tem por objetivo receber 6 valores, organizar em lista, somar os valores, calcular a media e determinar o maior e o menor valor.")

def coletaValores():
    global lista
    lista = []
    for i1 in range(6):
        lista.append(float(input("Digite o valor a adicionar à lista: ")))
    print(f"A lista criada é: {lista}")

def somaValores():
    global soma
    soma = 0
    for i in lista:
        soma = soma + i
    print(f"A soma dos valores é: {soma}")

def calculaMedia():
    global media
    media = soma/6
    print(f"A média dos valores é {media}")

def comparar():
    #maior valor
    maior = lista[1]
    for x in lista:
        if x>maior:
            maior=x
    print(f"O maior valor é: {maior}")

    #menor valor
    menor = maior
    for x in lista:
        if x<menor:
            menor=x
    print(f"O menor valor é: {menor}")


#Programa Principal
bemVindo()
coletaValores()
somaValores()
calculaMedia()
comparar()
