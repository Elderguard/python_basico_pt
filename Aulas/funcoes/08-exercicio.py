#----- Funções
def coletaPreco():
    global preco
    preco = float(input ("Valor do litro de combustivel: R$"))
    return preco

def  coletaQuantidade():
    global quantidade
    quantidade = float(input ("Quantidade de litros:"))
    return quantidade

def calculaConta():
    conta = preco*quantidade
    print("Conta: R$", conta)
    print("Conta2: R$ %.2f " % conta) #formatado com 2 casas decimais %.2f
    print(f"Conta3: R$ {conta}")
    

#----- Programa Principal
coletaPreco()
coletaQuantidade()
calculaConta()
