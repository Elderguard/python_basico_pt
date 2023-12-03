### DEFINIÇÃO DE VARIÁVEIS ###
lista1 = [1,2,3,4,9,6]
lista2 = [3,4,5,6,7,8]
interseccao = []


### FUNÇÕES ###
def bem_vindo():
    print("Bem vindo! Este programa tem por objetivo receber duas notas informadas pelo usuário, calcular a média e informar se a média final resulta em 'Aprovado' ou 'Reprovado'")

def encontrar_interseccao():
    for nro in lista1:
        if nro in lista2:
            interseccao.append(nro)

    print(interseccao)

### PROGRAMA PRINCIPAL ###
bem_vindo()
encontrar_interseccao()
