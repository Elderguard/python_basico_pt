"""
ATIVIDADE 2:

João e Maria resolveram jogar vídeo game, mas deveriam decidir quem começaria. João falou para decidirem na disputa do par ou ímpar e Maria aceitou. Então João e Maria iniciaram uma disputa de PAR ou ÍMPAR na qual cada um coloca uma certa quantidade de Dedos (de 0 até 5) cada um. Se a somatória for PAR então o João ganha. Se a somatória for PAR então o JOÃO ganha. Se a somatória for IMPAR então a Maria ganha. João sempre aposta em PAR e Maria sempre aposta em IMPAR.

Faça um programa que simule a disputa entre João e Maria para uma disputa de melhor de 5. Quem ganhar mais na disputa vence o jogo e começa jogando o vídeo-game.

RODADA  1   2   3   4   5
JOAO    2   4   1   0   3
MARIA   2   1   1   3   1
SOMA    4   5   2   3   4


"""
### DEFINIÇÕES DE VARIÁVEIS GLOBAIS
joao    = [2,4,1,0,3]
maria   = [2,1,1,3,1]
lista_soma    = []
escolha_joao    = 'PAR'
escolha_maria   = 'IMPAR'
vitorias_joao = 0
vitorias_maria = 0

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
    print('Olá, seja bem-vindo! Este software foi feito para simular um jogo de par ou ímpar realizado entre João e Maria.')


# Definindo a função separador_blocos que funcionará apenas como um detalhe visual de separar partes do programa
def separador_blocos(comprimento):
    print(comprimento*"-")

# Define a função que realiza a simulação das rodadas
def simular():
    for x in range(len(joao)):  # Cria um loop que repetirá na mesma quantidade de elementos que houver na lista de joão.
        separador_blocos(120)
        print(f'Na rodada {x}, João jogou {joao[x]} e Maria jogou {maria[x]}.')
        soma = joao[x]+maria[x]
        lista_soma.append(soma)
        resultado = testar_soma(soma)
        vencedor = definir_vencedor(resultado)
        print(f'O resultado é {resultado}. O vencedor é {vencedor}!')
        print(f'SCORE: João {vitorias_joao}     X     {vitorias_maria} Maria')

# Define a função testar_soma que verifica se é par ou ímpar.
def testar_soma(parametro_soma):
    if parametro_soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    
    return(resultado)

# Define a função definir_vencedor que determina quem vence de acordo com o resultado informado e incrementa o contador de vitórias
def definir_vencedor(resultado):
    if resultado == escolha_joao:   # Se o resultado for igual à escolha de joão
        vencedor = 'JOÃO'
        
        global vitorias_joao
        vitorias_joao = vitorias_joao+1
    
    else:   # Se não for igual à escolha de joão
        vencedor = 'MARIA' 
        
        global vitorias_maria
        vitorias_maria = vitorias_maria+1

    
    return(vencedor)


### PROGRAMA PRINCIPAL ###

imprimir_cabecalho('PAR OU ÍMPAR')
bem_vindo()
simular()
