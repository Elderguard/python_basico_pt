#Nro matricula: FFFCCCAASPMM

'''
FFF - codigo da faculdade
CCC - codigo do curso
AA - Ano de ingresso
S - Semestre
P - Período do curso
MM - Matrícula
'''

matricula=input("Nro matricula: ")
facul = matricula[0:3]
curso = matricula[3:6]
ano = matricula [6:8]
semestre = matricula [8:9]
print("Faculdade:", facul)
print("Curso:", curso)
print(f"Ano ingresso: 20{ano}")
print("Semestre:", semestre)