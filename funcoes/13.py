#Funções
def bemVindo():
    print("Bem vindo! Este programa tem por objetivo receber um valor informado pelo usuário, ler e responder se o valor é menor que 10, menor que 20, menor que 30 ou maior/igual a 30.")

def coletaVariavel():
    global x
    x = int(input("X = "))

def compararVariavel():
    if x<10:
        print("x é menor que 10")
    else:
        if x<20:
            print("x é menor que 20")
        else:
            if x<30:
                print("x é menor que 30")
            else:
                print("x é maior ou igual a 30")

#Programa Principal
bemVindo()
coletaVariavel()
compararVariavel()
