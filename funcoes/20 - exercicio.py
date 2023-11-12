#Import de bibliotecas
import sys

#Funções
def bemVindo():
    print("Bem vindo! Este programa tem por objetivo receber do usuário um código de estado para determinar o valor de imposto percentual cobrado.")

def identificaEstado():
    global codigo
    codigo = int(input("Digite o codigo do seu estado (1 a 6): "))

def defineImposto():
    if codigo == 1:
        imposto = 0.35
    elif codigo ==2:
        imposto = 0.25
    elif codigo ==3:
        imposto = 0.15
    elif codigo ==4:
        imposto = 0.10
    elif codigo ==5:
        imposto = 0.05
    elif codigo ==6:
        imposto = 0
    else:
        print("O código informado não existe, reinicie o programa")
        sys.exit()
        
    impPercentual = imposto*100
    print(f"O valor do imposto para o seu estado é de {impPercentual} %")


#Programa Principal
bemVindo()
identificaEstado()
defineImposto()
