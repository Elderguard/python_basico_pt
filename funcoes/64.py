#-------Funções
def maior(x,y,z):
    if x>y and x>z:
        print(x)
    elif y>z:
        print(y)
    else:
        print(z)

#-----Programa principal
a = int(input("Nro1: "))
b = int(input("Nro2: "))
c = int(input("Nro3: "))
maior(a,b,c)