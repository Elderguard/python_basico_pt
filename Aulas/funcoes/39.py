### DEFINIÇÃO DE VARIÁVEIS ###
alunos = []
media = []


### FUNÇÕES ###
def bem_vindo():
    print("Bem vindo! Este programa tem por objetivo receber nomes e medias de alunos e atribuí-los a listas.")

def coletar_dados():
    #ler 3 nomes de alunos e media de cada aluno

    for i in range(3):
        #ler nomes
        nome=input("Nome do aluno "+str(i+1)+": ")
        alunos.append(nome)
        #ler medias
        md = float(input("Media "+str(i+1)+"= "))
        media.append(md)
    print(30*"-")

def imprimir_dados():
    #imprimir dados
    for i in range(3):
        print("Nome: "+ alunos[i]+ " \nMedia: "+str(media[i]))
        separador()

def separador():
    print(30*"-")


### PROGRAMA PRINCIPAL ###
bem_vindo()
coletar_dados()
imprimir_dados()
