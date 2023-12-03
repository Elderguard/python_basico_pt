#Funções
def bemVindo():
    print("Bem vindo! Este programa tem por objetivo receber valores de peso e altura informadas pelo usuário, calcular o IMC e classificar retornando ao usuário a classificação.")

def coletaDados():
    global altura
    global peso
    altura = float(input("Digite sua altura em metros: "))
    print(f"A sua altura é: {altura} metros.")

    peso = float(input("Digite seu peso em Quilogramas (Kg): "))
    print(f"O seu peso é: {peso}Kg.")

def calculaIMC():
    global imc
    imc = peso/(altura**2)
    print("Seu IMC é igual a: %.2f" % imc)

def classificaIMC():
    if imc < 22:
        print("Você está magro")
    elif 22<=imc<=26:
        print("Você está normal")
    elif 26<imc<=30:
        print("Você está acima do peso")
    else:
        print("Você está obeso")

#Programa Principal
bemVindo()
coletaDados()
calculaIMC()
classificaIMC()
