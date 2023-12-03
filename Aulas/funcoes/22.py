#Funções
def bemVindo():
    print("Bem vindo! Este programa tem por objetivo receber um número de matrícula fictício de um aluno e retornar informações sobre o curso. Para isso, é considerada uma matrícula no seguinte padrão 'FFFCCCAASPMM', onde FFF representa o código da faculdade, CCC representa o código do curso, AA representa o ano de ingresso no curso, S representa o semestre de ingresso, P representa o período do curso e MM é o número individual do aluno da matrícula.")

def coletaMatricula():
    global matricula
    matricula=input("Nro matricula: ")

def identificadorDeCodigos():
    global facul
    global curso
    global ano
    global semestre
    facul = matricula[0:3]
    curso = matricula[3:6]
    ano = matricula [6:8]
    semestre = matricula [8:9]
    print("Faculdade:", facul)
    print("Curso:", curso)
    print(f"Ano ingresso: 20{ano}")
    print("Semestre:", semestre)

#Programa Principal
bemVindo()
coletaMatricula()
identificadorDeCodigos()
