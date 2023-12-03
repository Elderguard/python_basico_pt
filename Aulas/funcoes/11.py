# Funções
def bemVindo():
    print("Bem-vindo! Esse programa tem por objetivo coletar dois valores fornecidos pelo usuário e informar qual valor é maior.")

def coletaVariaveis():
    global a
    global b
    a = float(input("Digite o primeiro valor 'a': "))
    b = float(input("Digite o segundo valor 'b': "))

def compararVariaveis():
    if a>b:
        print (f"{a} é maior do que {b}")
    else:
        print (f"{b} é maior do que {a}")

#Programa principal
bemVindo()
coletaVariaveis()
compararVariaveis()
