nota1 = int(input("Digite a Nota 1: "))
nota2 = int(input("Digite a Nota 2: "))

media = (nota1+nota2)/2

if media<4:
    print("Reprovado")
elif 4<=media<6:
    print("Exame")
else:
    print("Aprovado")