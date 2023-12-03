#----- Import de bibliotecas
import math

#----- Funções
def coletaVariavel():
    global x
    x=int(input("Valor de x="))
    return x

def calculaRaiz(x):
    global rq
    rq = math.sqrt(x)
    print(rq)

#----- Programa Principal

coletaVariavel()
calculaRaiz(x)
