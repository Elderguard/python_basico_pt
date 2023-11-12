#Funções
def bemVindo():
    print("Bem vindo! Este programa tem por objetivo receber uma informação de idade do usuário, ler e responder se a idade é classificada como 'Bebê', 'Criança', 'Adolescente', 'Adulto' ou 'Idoso'")

def coletaIdade():
    global idade
    idade = int(input("Idade: "))

def classificar():
    if idade<5:
        print("Bebê")
    elif idade<12:
        print("Criança")
    elif idade<18:
        print( "Adolescente")
    elif idade<60:
        print("Adulto")
    else:
        print("Idoso")

#Programa Principal
bemVindo()
coletaIdade()
classificar()
