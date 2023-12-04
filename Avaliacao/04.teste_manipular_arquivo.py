"""
ATIVIDADE 3:

Fazer um programa em Python que leia o arquivo texto "Peso.txt" e:
A) Mostre os nomes e o peso de cada pessoa
B) Mostre o nome e o peso da pessoa mais pesada
C) Mostre o nome e o peso da pessoa menos pesada
D) Mostre a media dos pesos


"""
### DEFINIÇÃO DE VARIÁVEIS
indice_nome = None
indice_peso = None


### FUNÇÕES ###

# Definindo a função cabeçalho que receberá obrigatoriamente um texto a ser incluído no interior da tabela e outros parâmetros opcionais, tendo valores pre-determinados para caso os argumentos não sejam informados ao chamar a função
def imprimir_cabecalho(texto, comprimento = 120, espessura_lateral = 2, simbolo_horizontal = '-', simbolo_vertical = '|'):

    # Define uma variável utilizada para calcular a manipulação de centralização do texto
    centralizador = int(((comprimento-(4*espessura_lateral))/2)-len(texto)/2)

    print(simbolo_vertical * comprimento)       # Imprime o símbolo utilizado para as verticais na aresta superior da tabela
    print(simbolo_horizontal * comprimento)     # Imprime o símbolo utilizado para as horizontais na aresta superior da tabela
    print(simbolo_vertical * espessura_lateral, ' ' * centralizador, texto, ' ' * centralizador, simbolo_vertical * espessura_lateral)      # Imprime o texto centralizado
    print(simbolo_horizontal * comprimento)     # Imprime o símbolo utilizado para as horizontais na aresta inferior da tabela
    print(simbolo_vertical * comprimento)       # Imprime o símbolo utilizado para as verticais na aresta inferior da tabela


# Definindo a função bem_vindo que saudará e instruirá o usuário
def bem_vindo():
    print('\n')
    print('Olá, seja bem-vindo! Este software foi feito para ler informações em um arquivo e manipulá-las.')
    print('\n')


# Definindo a função separador_blocos que funcionará apenas como um detalhe visual de separar partes do programa
def separador_blocos(comprimento = 120):
    print(comprimento*"-")


# Definindo a função abrir_arquivo que abrirá o arquivo, fará a leitura atribuindo os valores lidos a uma variável e fechará o arquivo
def abrir_arquivo(nome_do_arquivo, variavel = None):
    #                          encoding foi usado como parâmetro para os caracteres serem reconhecidos.
    with open(nome_do_arquivo, encoding='utf-8') as variavel: # Abre o arquivo usando a variável 'variavel' para receber seu valor
        texto = variavel.read() # Realiza a leitura do arquivo e atribui o valor à variável local 'texto'
        variavel.close()        # Fecha o arquivo
        return(texto)           # Retorna o valor da variável local 'texto'


# Definindo a função que manipula o arquivo, tratando os dados
def tratar_arquivo(variavel):
    dados = separar_linhas(variavel)                                        # Chama a função separar_linhas e atribui seu retorno à variável local 'dados'
    dados_separados = separar_elementos_da_linha(dados)                     # Chama a função separar_elementos_da_linha e atribui seu retorno à variável local 'dados_separados'
    dados_tratados = remover_espacos_da_lista(dados_separados)              # Chama a função remover_espacos_da_lista e atribui seu retorno à variável local 'dados_tratados'
    identificar_titulos(dados_tratados)
    tornar_float(dados_tratados)                                            # Chama a função tornar_float sobre a lista 'dados_tratados'
    return(dados_tratados)                                                  # Retorna o valor de dados_tratados


# Definindo a função que separa as linhas do arquivo texto
def separar_linhas(variavel):
    dados = []                                                          # Cria uma variável local 'dados' do tipo lista, vazia.
    linhas = variavel.split('\n')                                       # Realiza a separação a partir dos elementos '\n' utilizados para quebra de linha, atribuindo à lista 'linhas'
    for row in linhas:                                                  # Realiza o empacotamento de cada linha da lista linhas e atribui à lista 'dados'
        split_linhas = row.split (",")
        dados.append(split_linhas)
    return(dados)                                                       # Retorna o valor de 'dados'
    

# Analisa os elementos em linha e separa a partir do caracter definido
def separar_elementos_da_linha(lista, car = ' '):
    elementos = []                                                      # Cria uma variável local 'elementos' do tipo lista, vazia.
    for i in range(len(lista)):                                         # Realiza uma iteração para separar os elementos a partir do caracter definido e atribuir à lista 'elementos'
        linha = lista[i]
        elementos.append(linha[0].split(car))
    return(elementos)                                                   # Retorna o valor de 'elementos'


# Analisa as listas e remove espaços vazios
def remover_espacos_da_lista(lista):
    filtragem_listas_vazias = []                                        # Cria uma variável local 'filtragem_listas_vazias' do tipo lista, vazia
    filtragem_vazios = []                                               # Cria uma variável local 'filtragem_vazios' do tipo lista, vazia
    
    for i in range(len(lista)):                                         # Realiza uma iteração para localizar listas de valor não vazio e atribui à lista 'filtragem_listas_vazias' 
        lista_vazia = ['']
        if lista[i] != lista_vazia:
            filtragem_listas_vazias.append(lista[i])

    for i in range(len(filtragem_listas_vazias)):                       # Realiza uma iteração para localizar valores não vazios na lista aninhada e atribui à lista 'filtragem_vazios'
        vazio = ''
        pequena_lista = []
        for j in range(len(filtragem_listas_vazias[i])):
            if filtragem_listas_vazias[i][j] != vazio:
                pequena_lista.append(filtragem_listas_vazias[i][j])
        filtragem_vazios.append(pequena_lista)

    return(filtragem_vazios)                                            # Retorna o valor de 'filtragem_vazios'


# Define a função tornar_float que lerá os valores no índice 1 das listas aninhadas e transformará esses valores em float
def tornar_float(lista):
    for i in range(1,len(lista)):
        lista[i][indice_peso] = float(lista[i][indice_peso])


# Identifica o índice do peso e nome
def identificar_titulos(lista):
    global indice_nome
    global indice_peso
    lista[0][0] = lista[0][0].upper()
    lista[0][1] = lista[0][1].upper()
    indice_peso = lista[0].index('PESO')
    indice_nome = lista[0].index('NOME')


# Define a função imprimir_nome_e_peso que mostrará no terminal uma listagem dos nomes e pesos de cada indivíduo da lista
def imprimir_nome_e_peso(lista):
    separador_blocos()
    print(f'Abaixo será listado o {lista[0][indice_nome]} e {lista[0][indice_peso]} de cada pessoa:')
    for i in range(1, len(lista)):
        print(f'O {lista[0][indice_nome]} do {i}° indivíduo da lista é {lista[i][indice_nome]} e seu peso é de {lista[i][indice_peso]}Kg.')


# Define a função definir_maior_peso que fará procedimentos para encontrar o maior valor entre os pesos dos indivíduos e o respectiovo nome
def definir_maior_peso(lista):
    separador_blocos()
    maior = 0.0
    nome_maior = 'Se você vir este texto, algo deu errado na execução'

    for i in range(1,len(lista)):
        comparador = lista[i][indice_peso]
        if maior < comparador:
            maior = lista[i][indice_peso]
            nome_maior = lista[i][indice_nome]
    print(f'O maior peso encontrado foi de {maior}Kg, do indivíduo de nome {nome_maior}!')


# Define a função definir_menor_peso que fará procedimentos para encontrar o menor valor entre os pesos dos indivíduos e o respectivo nome
def definir_menor_peso(lista):
    separador_blocos()
    menor = 1000
    nome_menor = 'Se você vir este texto, algo deu errado na execução'

    for i in range(1,len(lista)):
        comparador = lista[i][indice_peso]
        if menor > comparador:
            menor = lista[i][indice_peso]
            nome_menor = lista[i][indice_nome]
    print(f'O maior peso encontrado foi de {menor}Kg, do indivíduo de nome {nome_menor}!')


# Define a função calcular_media que somará os valores do índice 1 das listas aninhadas e dividirá pelo tamanho da lista geral para encontrar a media.
def calcular_media(lista):
    separador_blocos()
    soma = 0
    media = 0
    
    for i in range(1, len(lista)):
        soma = soma + lista[i][indice_peso]
    media = soma/(len(lista)-1)
    print('A média de pesos dos indivíduos é de: %.2f' % media + 'Kg.')


### PROGRAMA PRINCIPAL ###

imprimir_cabecalho('EXERCÍCIO 3 ')
bem_vindo()
arquivo = abrir_arquivo('./Avaliacao/teste.txt')
arquivo_tratado = tratar_arquivo(arquivo)

# ATENDENDO AO ITEM A DO EXERCÍCIO:
imprimir_nome_e_peso(arquivo_tratado)

# ATENDENDO AO ITEM B DO EXERCÍCIO:
definir_maior_peso(arquivo_tratado)

# ATENDENDO AO ITEM C DO EXERCÍCIO:
definir_menor_peso(arquivo_tratado)

# ATENDENDO AO ITEM D DO EXERCÍCIO:
calcular_media(arquivo_tratado)