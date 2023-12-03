alunos = []
media = []
#ler 3 nomes de alunos e media de cada aluno

for i in range(3):
    nome=input("Nome do aluno "+str(i)+" :")
    alunos.append(nome)
    md = float(input("Media "+str(i)+" ="))
    media.append(md)

#imprimir dados
for i in range(3):
    print("Nome: "+ alunos[i]+ " \nMedia: "+str(media[i]))
