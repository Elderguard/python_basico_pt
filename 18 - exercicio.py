import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b**2) - 4*a*c

print(delta)

if delta<0:
    print("Não existem raízes reais")

else:
    print("Existem raízes reais")
    x1= (-b+math.sqrt(delta))/(2*a)*(-1)
    x2= (-b-math.sqrt(delta))/(2*a)*(-1)

    print("X1 = ",x1)
    print("X2 = ",x2)