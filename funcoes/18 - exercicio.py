#Import de bibliotecas
import math

#Funções
def bemVindo():
    print("Bem vindo! Este programa tem por objetivo calcular as raízes de uma equação de 2° grau no formato 'a*x + b*x² + c = 0', a partir dos valores informados pelo usuário.")

def coletaValores():
    global a
    global b
    global c
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

def calculaDelta():
    global delta
    delta = (b**2) - 4*a*c
    print(delta)

def calculaRaiz():
    if delta<0:
        print("Não existem raízes reais")

    else:
        print("Existem raízes reais")
        x1= (-b+math.sqrt(delta))/(2*a)*(-1)
        x2= (-b-math.sqrt(delta))/(2*a)*(-1)

        print("X1 = ",x1)
        print("X2 = ",x2)


#Programa Principal
bemVindo()
coletaValores()
calculaDelta()
calculaRaiz()
