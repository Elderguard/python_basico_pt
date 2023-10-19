alunos = []
#ler 5 nomes de alunos

for i in range(5):
    nome=input("Nome do aluno "+str(i)+" :")
    alunos.append(nome)

#imprimir dados
print(alunos)
for nome in alunos:
    print(nome)
