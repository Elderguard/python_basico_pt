### DEFINIÇÃO DE VARIÁVEIS ###
produto1 = ["Água", 4, 2.50]
produto2 = ["Suco", 3, 5.00]
produto3 = ["café", 2, 4.50]
produtos = [produto1,produto2,produto3]
total = []
totalGeral=0


### FUNÇÕES ###
def bem_vindo():
    print("Bem vindo! Este programa tem por objetivo ler valores em listas e realizar um calculo hipotético do preço de mercadorias.")

def calcular_precos():
    for i in range(len(produto1)):
        global totalGeral
        total.append(produtos[i][1]*produtos[i][2])
        print("Total " + produtos[i][0], "= R$ %.2f" % total[i])
        totalGeral= totalGeral + total[i]

    print("Total Geral ", "= R$ %.2f" % totalGeral)


### PROGRAMA PRINCIPAL ###
bem_vindo()
calcular_precos()
