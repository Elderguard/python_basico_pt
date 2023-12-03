### DEFINIÇÃO DE VARIÁVEIS ###

alunos = []


### FUNÇÕES ###

def bem_vindo():
    print("Bem vindo! Este programa tem por objetivo receber valores informados pelo usuário e incluir em uma lista.")

def coletar_dados():
    #coletar dados
    for i in range(5):
        nome=input("Nome do aluno: ")
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
