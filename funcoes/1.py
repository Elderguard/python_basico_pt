#-----Variaveis iniciais
A1 = 10
A2 = 2

B1 = -5

C1 = 5
C = 0

nota1 = 9.6
nota2 = 3

D1 = 34
D2 = 3

#-----Funções
def soma(): #soma os valores predefinidos de A1 e A2
    global A
    A = A1 + A2
    print("A=", A)
    return A

def subtracao(): #subtrai os valores predefinidos de A e B1
    global B
    B = A - B1
    print("B=", B)
    return B

def multiplicacao(): #multiplica os valores predefinidos de C1 com a soma de A+B
    global C
    C = C1 * (A+B)
    print("C=", C)
    return C

def calculaMedia(): #calcula a media de dois valores predefinidos
    global media
    media = (nota1+nota2)/2
    print("media=", media)
    return media

def restoDeDivisao(): #calcula e mostra o resto de Divisao dos valores predefinidos de D1 e D2
    global D
    D = D1 % D2
    print("D=", D)
    return D

def divisao(): #calcula e mostra o resultado da divisao dos valores predefinidos de D1 e D2
    global E
    E = D1 / D2
    print("E=", E)
    return E

def divisaoInteira(): #calcula e mostra a parte inteira da divisao dos valores predefinidos de D1 e D2
    global F
    F = D1 // D2
    print("F=", F)
    return F

def potencia(): #calcula e mostra a potencia do valor predefinido de A1 ao expoente predefinido A2
    global G
    G = A1**A2
    print("G=", G)
    return G

#-----Programa principal
soma()
subtracao()
multiplicacao()
calculaMedia()
restoDeDivisao()
divisao()
divisaoInteira()
potencia()