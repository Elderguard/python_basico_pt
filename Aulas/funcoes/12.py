#Funções
def bemVindo():
    print("Bem vindo! Este programa tem por objetivo receber uma informação do usuário 'F' ou 'M' ler e responder com 'Feminino' ou 'Masculino'")

def coletaInfo():
    global sexo
    sexo = input("Informe o sexo (M/F)")

def compararInfo():
    if sexo =="F" or sexo =='f':
        print( "Feminino")
    elif sexo =="M" or sexo =='m':
        print( "Masculino") 
    else:
        print("A informação enviada não corresponde aos parâmetros esperados.")

#Programa Principal
bemVindo()
coletaInfo()
compararInfo()
