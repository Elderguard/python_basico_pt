### DEFINIÇÃO DE VARIÁVEIS ###
lista = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []

### FUNÇÕES ###
def bem_vindo():
    print("Bem vindo! Este programa tem por objetivo receber um valor informado pelo usuário e usá-lo como range para a criação de novas listas.")

def coletar_valor():
    global intervalo
    intervalo = int(input('Informe o valor para o range(intervalo)'))

def criar_lista_dobro():
    lista = [x*2 for x in range(intervalo)]
    print(lista)

def criar_lista_pot_quadrada():
    lista2 = [x**2 for x in range(intervalo)]
    print(lista2)

def criar_lista_restos_por_2():
    lista3 = [x%2 for x in range(intervalo)]
    print(lista3)

def criar_lista_x_por_4():
    k=4
    lista4 = [x*k for x in range(intervalo)]
    print(lista4)

def criar_lista_exp_base2():
    lista5 = [2**x for x in range(intervalo)]
    print(lista5)


### PROGRAMA PRINCIPAL ###
bem_vindo()
coletar_valor()
criar_lista_dobro()
criar_lista_pot_quadrada()
criar_lista_restos_por_2()
criar_lista_x_por_4()
criar_lista_exp_base2()
