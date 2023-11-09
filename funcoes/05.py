#----- Variáveis
codigo = 135
nome = "Maria Antonieta"
ativo = True
salario = 1320.00

#----- Funções
def imprimeCodigo(codigo):
    print("código = %d" % codigo) # %d é para dado tipo int, mostra número inteiro

def imprimeNome(nome):
    print("Nome: = %s" % nome) # %s é para tipo char, mostra cadeia de caracteres

def imprimeStatus(ativo):
    print("Ativo = %r" % ativo) # %r é para tipo boolean, mostra true or false

def imprimeSalario(salario):
    print("Salário = %.2f" % salario) # %f é para float ou double, mostra número decimal

#----- Programa Principal

imprimeCodigo(codigo)
imprimeNome(nome)
imprimeStatus(ativo)
imprimeSalario(salario)

