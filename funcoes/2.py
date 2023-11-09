#-----funções
def coletaNome():
    global nome
    nome = str(input("Nome do funcionário: "))
    print(type(nome))
    return nome

def coletaSalario():
    global salario
    salario = float(input("Salário do funcionário: R$"))
    print(type(salario))
    return salario

def imprimeInformacao():
    print(f"{nome} recebe {salario} por mês")

#-----Programa principal
coletaNome()
coletaSalario()
imprimeInformacao()
