#FUNÇÃO QUE RETORNA VALOR

#-------Funções
def calculaIMC(peso, altura):
    IMC = peso/(altura**2)
    print(IMC)
    return IMC

def classificaIMC(IMC):
    if IMC<18.5:
        print("Você está magro")
    elif 18.5<=IMC<25:
        print("Você está Normal")
    elif 25<=IMC<30:
        print("Você está em situação de Sobrepeso")
    else:
        print("Você está Obeso")

#-----Programa principal
peso = float(input("Informe o peso de quem deseja calcular o IMC: "))
altura = float(input("Informe a altura de quem deseja calcular o IMC: "))
IMC = calculaIMC(peso, altura)
classificaIMC(IMC)