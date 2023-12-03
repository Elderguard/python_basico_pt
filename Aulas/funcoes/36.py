### DEFINIÇÃO DE VARIÁVEIS GLOBAIS ###

valores=[0,0,0]

### FUNÇÕES ###
def bem_vindo():
    print("Bem vindo! Este programa tem por objetivo receber valores informados pelo usuário e incluí-los em uma lista.")

def coletar_valores():
    x = 0
    while x<3:
        valores[x] = int(input('Valor: '))
        x = x + 1
    print(f"Os valores informados foram: {valores}")

#### PROGRAMA PRINCIPAL ###
bem_vindo()
coletar_valores()
