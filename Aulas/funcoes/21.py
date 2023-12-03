# Import de bibliotecas
import sys

#Funções
def bemVindo():
    print("Bem vindo! Este programa tem por objetivo receber o nome completo de um usuário e retornar a quantidade de caracteres do nome e a quantidade de ocorrências de uma letra também informada pelo usuário.")

def coletaNome():
    global nome
    nome=input("Nome completo:")

def identificaTamanho():
    tam=len(nome)
    print("Nro de caracteres da frase:", tam)

def defineCaracter():
    global car
    car = input("Informe qual caractere quer saber quantas vezes está presente no texto informado: ")

def contaCaracter():
    print("Nro de ocorrências da letra a:", nome.count(car))

#Programa Principal
bemVindo()
coletaNome()
identificaTamanho()
defineCaracter()
contaCaracter()
