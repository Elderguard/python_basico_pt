### DEFINIÇÃO DE VARIÁVEIS ###
alunos = []
media = []


### FUNÇÕES ###
def bem_vindo():
    print("Bem vindo! Este programa tem por objetivo receber nomes e medias informados pelo usuário e atribuí-los em listas. Além disso, o programa deve encontrar e informar a maior média e a quem pertence.")

def coletar_dados():
    #ler 4 nomes de alunos e media de cada aluno
    for i in range(4):
        #coletar nomes
        nome=input("Nome do aluno "+str(i+1)+": ")
        alunos.append(nome)
        #coletar medias
        md = float(input("Media "+str(i+1)+"= "))
        media.append(md)
    print(30*"-")

def imprimir_dados():
    #imprimir dados
    for i in range(4):
        print("Aluno "+str(i)+": \nNome: "+ alunos[i]+ " \nMedia: "+str(media[i]))
        print(30*"-")

def encontrar_maior():
    #encontrar maior media e o nome do aluno
    maior = -1
    posmaior = -1

    for i in range(4):
        if media[i]>maior:
            maior=media[i]
            posmaior=i
    #imprime resultado
    print("Maior media = ",maior)
    print("Nome do aluno: ", alunos[posmaior])


### PROGRAMA PRINCIPAL ###
bem_vindo()
coletar_dados()
imprimir_dados()
encontrar_maior()
