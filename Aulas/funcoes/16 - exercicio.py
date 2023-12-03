#Funções
def bemVindo():
    print("Bem vindo! Este programa tem por objetivo receber duas notas informadas pelo usuário, calcular a média e informar se a média final resulta em 'Aprovado' ou 'Reprovado'")

def coletaNotas():
    global nota1
    global nota2
    nota1 = int(input("Digite a Nota 1: "))
    nota2 = int(input("Digite a Nota 2: "))

def calculaMedia():
    global media
    media = (nota1+nota2)/2

def mostraResultado():
    if media<6:
        print("Reprovado")
    else:
        print("Aprovado")


#Programa Principal
bemVindo()
coletaNotas()
calculaMedia()
mostraResultado()
