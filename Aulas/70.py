#FUNÇÃO QUE RETORNA VALOR

#-------Funções
def calculaIMC(peso, altura):
    IMC = peso/(altura**2)
    return IMC

#-----Programa principal
peso = float(input("Informe o peso de quem deseja calcular o IMC: "))
altura = float(input("Informe a altura de quem deseja calcular o IMC: "))
IMC = calculaIMC(peso, altura)

print(IMC)