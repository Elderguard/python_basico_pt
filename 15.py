idade = int (input("Idade: "))

if idade<5:
    print("Bebe")
elif idade<12:
    print("Criança")
elif idade<18:
    print( "Adolescente")
elif idade<60:
    print("Adulto")
else:
    print("Idoso")