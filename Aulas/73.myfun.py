#VER NO SLIDE CRIAR FUNCAO


#-------Funções
def Maior(a, b):
    if a>b:
        return(a)
    else:
        return(b)
    
def Menor (a,b):

impo
#-----Programa principal
peso = float(input("Informe o peso de quem deseja calcular o IMC: "))
altura = float(input("Informe a altura de quem deseja calcular o IMC: "))
IMC = calculaIMC(peso, altura)
classificaIMC(IMC)