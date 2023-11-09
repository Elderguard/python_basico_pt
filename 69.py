#FUNÇÃO QUE RETORNA VALOR

#-------Funções
def AreaQuadrado(L):
    Areaq =L*L
    return(Areaq)

#-----Programa principal
lado = int(input("Lado: "))
Area = AreaQuadrado(lado)

print("Area = ", Area)