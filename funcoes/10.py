#----- Funções

def bemVindo():
    print("Este programa tem por objetivo calcular a porcentagem de votos de cada candidato entre 3 candidatos de uma eleição")

def coletaCandidato1():
    global candidato1 
    global nrovotos1
    candidato1 = input("Nome do candidato 1:")
    nrovotos1 = int(input("Nro de votos do candidato 1: "))

def coletaCandidato2():
    global candidato2 
    global nrovotos2
    candidato2 = input("Nome do candidato 2:")
    nrovotos2 = int(input("Nro de votos do candidato 2: "))

def coletaCandidato3():
    global candidato3 
    global nrovotos3
    candidato3 = input("Nome do candidato 3:")
    nrovotos3 = int(input("Nro de votos do candidato 3: "))

def calculaVotos():
    #Total de votos
    global totalvotos
    totalvotos = nrovotos1 + nrovotos2 + nrovotos3
    
    #Fração de cada candidato
    global porc_votos1
    global porc_votos2
    global porc_votos3
    porc_votos1 = (nrovotos1/totalvotos)*100
    porc_votos2 = (nrovotos2/totalvotos)*100
    porc_votos3 = (nrovotos3/totalvotos)*100

    #Percentual de cada candidato
    # porc_votos1 = frac_votos1*100
    # porc_votos2 = frac_votos2*100
    # porc_votos3 = frac_votos3*100


def imprimeVotos():
    #Total de votos
    print("\n")
    print ("Total de votos: ", totalvotos)
    
    #Votos por candidato
    print("\n")
    print(f"Votos do candidato 1: {nrovotos1}")
    print(f"Votos do candidato 2: {nrovotos2}")
    print(f"Votos do candidato 3: {nrovotos3}")

    #Porcentagem de votos por candidato
    print("\n")
    print ("Porcentagem de votos 1: %.2f" % porc_votos1, " %")
    print ("Porcentagem de votos 2: %.2f" % porc_votos2, " %")
    print ("Porcentagem de votos 3: %.2f" % porc_votos3, " %")


#----- Programa Principal
bemVindo()
coletaCandidato1()
coletaCandidato2()
coletaCandidato3()
calculaVotos()
imprimeVotos()
