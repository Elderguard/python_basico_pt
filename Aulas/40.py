alunos = []
media = []
#ler 4 nomes de alunos e media de cada aluno

for i in range(4):
    nome=input("Nome do aluno "+str(i)+" :")
    alunos.append(nome)
    md = float(input("Media "+str(i)+" ="))
    media.append(md)

#imprimir dados
for i in range(4):
    print("Aluno "+str(i)+": \nNome: "+ alunos[i]+ " \nMedia: "+str(media[i]))

#encontrar maior media e o nome do aluno
maior = -1
posmaior = -1

for i in range(4):
    if media[i]>maior:
        maior=media[i]
        posmaior=i

print("Maior media = ",maior)
print("Nome do aluno: ", alunos[posmaior])