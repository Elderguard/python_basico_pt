preco = float(input ("Valor do litro de combustpivel: R$"))
quantidade = float(input ("Quantidade de litros:"))

conta = preco*quantidade

print("Conta: R$", conta)
print("Conta2: R$ %.2f " % conta) #formatado com 2 casas decimais %.2f
print(f"Conta3: R$ {conta}")
