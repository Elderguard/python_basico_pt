#----- Funções

def coletaNome():
    global nome
    nome = input("Digite o nome do usuário: ")
    return nome

def mensagemBemVindo():
    print(f"Olá {nome}, seja bem-vindo(a)!")

def mostrarValor(valor):
    print("Valor = ", valor)

def mostrar2Decimais(valor):
    print('Valor = %.2f' % valor)

def mostrar3Decimais(valor):
    print(f"Valor= {valor:.3f}")


#----- Código principal

coletaNome()
mensagemBemVindo()

valor = 3.1415
mostrarValor(valor)
mostrar2Decimais(valor)
mostrar3Decimais(valor)
