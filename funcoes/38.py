### DEFINIÇÃO DE VARIÁVEIS ###
alunos = []


### FUNÇÕES ###
def bem_vindo():
    print("Bem vindo! Este programa tem por objetivo receber nomes informados pelo usuário e adicionálos a uma lista.")

def coletar_dados():
    #ler 5 nomes de alunos
    for i in range(5):
        nome=input("Nome do aluno "+str(i+1)+": ")
        alunos.append(nome)

def imprimir_dados():
    #imprimir dados
    print(alunos)
    for nome in alunos:
        print(nome)


### PROGRAMA PRINCIPAL ###
bem_vindo()
coletar_dados()
imprimir_dados()
