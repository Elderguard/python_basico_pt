#----- Import de bibliotecas
import math

#----- Funções
def coletaVariavel():
    global x
    x=int(input("Valor de x="))
    return x

def potencia(x):
    pot = math.pow(x,2)
    print(pot)

#----- Programa Principal
coletaVariavel()
potencia(x)
