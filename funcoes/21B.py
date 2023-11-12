# Import de bibliotecas
import sys

#Funções
def bemVindo():
    print("Bem vindo! Este programa tem por objetivo receber o nome completo de um usuário e retornar com o texto completamente em maiúsculo ou minúsculo.")

def coletaNome():
    global nome
    nome=input("Nome completo:")

def defineAcao():
    global acao
    acao = int(input("Digite 1 para transformar o texto em maiúsculo ou 2 para transformar o texto em minúsculo: "))

def transformar():
    if acao == 1:
        print(nome.upper())
    elif acao == 2:
        print(nome.lower())
    else:
        print("A informação digitada não corresponde aos parâmetros esperados.")

#Programa Principal
bemVindo()
coletaNome()
defineAcao()
transformar()
