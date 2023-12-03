valores=[0,0,0]

x=0
while x < 3:
    valores[x] = int(input("Valor: "))
    x=x+1
print(valores)

valores.append(5)

print(valores)
