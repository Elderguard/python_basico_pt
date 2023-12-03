### DEFINIÇÃO DE VARIÁVEIS ###
animais = ["cachorro", "gato", "macaco", "gavião"]


### FUNÇÕES ###
def bem_vindo():
    print("Bem vindo! Este programa tem por objetivo ler uma lista e informar o índice em que se encontra um elemento.")

def encontrar_indice():
    indice_gato = animais.index("gato")
    print(indice_gato)


### PROGRAMA PRINCIPAL ###
bem_vindo()
encontrar_indice()
