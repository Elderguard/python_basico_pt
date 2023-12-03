"""
ATIVIDADE 1:

FAZER UMA FUNÇÃO QUE CALCULE O MONTANTE DE UMA APLICAÇÃO FINANCEIRA, SABENDO-SE QUE:

    Montante = Capital * (1 + taxa_juro)^N

Onde: 
    Capital é o valor aplicado
    taxa_juro é a taxa mensal de juros
    N é o número de meses da aplicação

Obs: montar uma tabela mostrando o valor do montante a cada mês.
"""
### DEFINIÇÕES INICIAIS

nome_instituicao = "FATEC-ARARAQUARA"   # Atribui uma string à variável nome_instituicao que será usada no cabeçalho mais à frente

### PROPRIEDADES DA TABELA ###

comprimento_da_tabela = 120     # variável usada para definir o comprimento da tabela que será criada, em espaços de caracter
espessura_da_tabela = 2         # variável usada para definir a espessura da tabela que será criada, em espaços de caracter


### FUNÇÕES ###

# Definindo a função cabeçalho que receberá obrigatoriamente um texto a ser incluído no interior da tabela e outros parâmetros opcionais, tendo valores pre-determinados para caso os argumentos não sejam informados ao chamar a função
def imprimir_cabecalho(texto, comprimento = comprimento_da_tabela, espessura_lateral = espessura_da_tabela, simbolo_horizontal = '-', simbolo_vertical = '|'):

    # Define uma variável utilizada para calcular a manipulação de centralização do texto
    centralizador = int(((comprimento-(4*espessura_lateral))/2)-len(texto)/2)

    print(simbolo_vertical * comprimento)       # Imprime o símbolo utilizado para as verticais na aresta superior da tabela
    print(simbolo_horizontal * comprimento)     # Imprime o símbolo utilizado para as horizontais na aresta superior da tabela
    print(simbolo_vertical * espessura_lateral, ' ' * centralizador, texto, ' ' * centralizador, simbolo_vertical * espessura_lateral)      # Imprime o texto centralizado
    print(simbolo_horizontal * comprimento)     # Imprime o símbolo utilizado para as horizontais na aresta inferior da tabela
    print(simbolo_vertical * comprimento)       # Imprime o símbolo utilizado para as verticais na aresta inferior da tabela


# Definindo a função bem_vindo que saudará e instruirá o usuário
def bem_vindo():
    texto = ['Olá, seja bem-vindo! Este software foi feito para calcular o montante de uma aplicação financeira.','Para isso, é necessário que informe os seguintes dados: ','-> CAPITAL: valor em dinheiro a ser aplicado; ','-> TAXA DE JUROS (%): valor percentual mensal que agirá sobre o dinheiro aplicado;','-> TEMPO: Quantidade de meses que durará a aplicação. ']    # Cria uma lista com os textos que deverão ser mostrados ao usuário
    return(texto)    # Retorna o valor da lista


# Definindo a função tabelar que receberá um argumento obrigatório de lista de textos e imprimirá em uma tabela, de forma centralizada, além de parâmetros opcionais, tendo valore pre-determinados para caso os argumentos não sejam informados ao chamar a função
def tabelar(texto, comprimento = comprimento_da_tabela, espessura_lateral = espessura_da_tabela, simbolo_vertical = '|', list=None):
    
    # Cria o loop para percorrer a lista e executar as instruções
    for x in range(len(texto)):
        centralizador = int(((comprimento-(4*espessura_lateral))/2)-len(texto[x])/2)    # Definie uma variável utilizada para calcular a manipulação de centralização do texto
        print(simbolo_vertical * espessura_lateral, ' ' * centralizador, texto[x], ' ' * centralizador, simbolo_vertical * espessura_lateral) # Imprime de forma centralizada


# Definindo a função separador_blocos que funcionará apenas como um detalhe visual de separar partes do programa
def separador_blocos(comprimento):
    print(comprimento*"-")


def coletar_dados():
    global aplicacao    # Define uma variável global aplicacao

    # Define aplicacao como um dicionário e atribui chaves com o valor None
    aplicacao = {'capital':None, 'taxa_juro':None, 'meses':None }

    # Pede ao usuário que forneça os valores que serão adicionados ao dicionário
    aplicacao['capital'] = float(input('Por favor, informe o CAPITAL a ser aplicado: '))
    aplicacao['taxa_juro'] = float(input("Por favor, informe a TAXA DE JUROS (%) a ser aplicada: "))
    aplicacao['meses'] = int(input("Por favor, informe o TEMPO de aplicação: "))
        

# Define a função calcular_montante que fará o calculo do valor do montante a cada mês e adicionará a uma lista, de forma filtrada.
def calcular_montante():
    global lista_montantes  # Define a variável global lista_montantes
    lista_montantes = []    # Atribui à variável lista_montantes o valor de uma lista vazia

    for x in range(1,aplicacao['meses']+1): # Executa um loop a partir do índice 1 até meses+1
        montante = aplicacao['capital'] * (1 + aplicacao['taxa_juro']/100)**x   # Calcula e atribui à variável montante o valor em determinado momento do loop
        lista_montantes.append('Mês %.3i' % x + ': %.2f' % montante)            # Adiciona o valor momentâneo de montante ao final da lista_montantes


### PROGRAMA PRINCIPAL ###

imprimir_cabecalho(nome_instituicao)
tabelar(bem_vindo())
separador_blocos(comprimento_da_tabela)
coletar_dados()
separador_blocos(comprimento_da_tabela)
imprimir_cabecalho('SIMULADOR DE APLICAÇÃO')
calcular_montante()
tabelar(lista_montantes)
separador_blocos(comprimento_da_tabela)