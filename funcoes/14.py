#Funções
def bemVindo():
    print("Bem vindo! Este programa tem por objetivo receber uma informação de idade do usuário, ler e responder se a idade é classificada como 'Adolescente', 'Adulto' ou 'Idoso'")

def coletaIdade():
    global idade
    idade = int(input("Idade: "))

def classificar():
    if idade<18:
        print( "Adolescente")
    elif idade<60:
        print("Adulto")
    else:
        print("Idoso")


#Programa Principal
bemVindo()
coletaIdade()
classificar()
