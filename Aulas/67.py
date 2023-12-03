#PARAMETROS OPCIONAIS

#-------Funções
def cabecalho(car = '*', n=10):
    print(car * n)
    print(car * 2, ' ' * 8, 'FATEC-ARARAQUARA', ' ' * 8, car * 2)
    print(car * n)

#-----Programa principal
cabecalho()
cabecalho('#')
cabecalho('x', 40)