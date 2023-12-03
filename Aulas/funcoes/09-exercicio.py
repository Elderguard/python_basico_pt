#----- Funções

def bemVindo():
    print("Olá, este programa foi feito para calcular o IMC com base no peso e altura de uma pessoa. \n")

def coletaPeso():
    global peso
    peso = float(input("Informe seu peso em Quilogramas (Kg): "))
    return peso

def coletaAltura():
    global altura
    altura = float(input("Informe sua altura em metros (m): "))
    return altura

def calculaIMC():
    global iMC
    iMC = peso/(altura**2)
    print("IMC: ", iMC)
    print("IMC2: %.2f " % iMC) #formatado com 2 casas decimais %.2f
    print(f"IMC3: {iMC}")

#----- Programa Principal
bemVindo()
coletaPeso()
coletaAltura()
calculaIMC()
