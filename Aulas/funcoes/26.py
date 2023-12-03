#Funções
def bemVindo():
    print("Bem vindo! Este programa tem por objetivo receber e organizar em lista 6 dados informados pelo usuário, mostrando a lista ao fim.")

def coletaDados():
    global lista
    lista = []
    for x in range(6):
        lista.append(input("Informe o dado a ser adicionado: "))

def imprimeLista():
        print(lista)
        
#Programa Principal
bemVindo()
coletaDados()
imprimeLista()
