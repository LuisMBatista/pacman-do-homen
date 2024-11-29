from pacman import *
import time     

def obtem_direcao(ponto1, ponto2):
    theta = math.atan2(ponto1[1] - ponto2[1], ponto1[0] - ponto2[0])
    dir_x = math.cos(theta)
    dir_y = math.sin(theta)
    return dir_x, dir_y

###########################################################################################################################################

# definir orientação e movimentação
def pacman_cima(estado_jogo):
    estado_jogo['pacman']['direcao_atual'] = (0, 5)
    estado_jogo['pacman']['objeto'].setheading(90)  # Rotaciona para cima.
    print (estado_jogo['pacman']['objeto'].heading())

def pacman_baixo(estado_jogo):
    estado_jogo['pacman']['direcao_atual'] = (0, -5)
    estado_jogo['pacman']['objeto'].setheading(270)  # Rotaciona para baixo.
    print (estado_jogo['pacman']['objeto'].heading())

def pacman_direita(estado_jogo):
    estado_jogo['pacman']['direcao_atual'] = (5, 0)
    estado_jogo['pacman']['objeto'].setheading(0)  # Rotaciona para direita.
    print (estado_jogo['pacman']['objeto'].heading())

def pacman_esquerda(estado_jogo):
    estado_jogo['pacman']['direcao_atual'] = (-5, 0)
    estado_jogo['pacman']['objeto'].setheading(180)  # Rotaciona para esquerda.
    print (estado_jogo['pacman']['objeto'].heading())


import turtle
#definir botões do teclado para jogar
tela = turtle.Screen()
tela.listen()  

tela.onkeypress(lambda: pacman_cima(estado_jogo), "Up")
tela.onkeypress(lambda: pacman_baixo(estado_jogo), "Down")
tela.onkeypress(lambda: pacman_direita(estado_jogo), "Right")
tela.onkeypress(lambda: pacman_esquerda(estado_jogo), "Left")

###########################################################################################################################################

def movimenta_pinky(estado_jogo):
    pass


def calculate_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def movimenta_clyde(estado_jogo):
    scatter_distance_threshold = 3
    scatter_corner_index = 0
    pacman_pos = estado_jogo['pacman']['objeto'].pos()
    ghost_pos = estado_jogo['fantasmas'][CLYDE_OBJECT]['objeto'].pos()
    
    return 


def movimenta_inky(estado_jogo):
    pass


def movimenta_blinky(estado_jogo):
    pass

def perdeu_jogo(estado_jogo):
    pass

def atualiza_pontos(estado_jogo):
    x = estado_jogo['pacman']['objeto'].xcor() 
    y = estado_jogo['pacman']['objeto'].ycor()
    index = offset((x,y))
    if estado_jogo['mapa'][index] == 1:
        estado_jogo['score'] += 1
        estado_jogo['mapa'][index] = 7
        x, y = calcula_x_y_from_index(index)
        estado_jogo['marcador'].goto(x + 10,y + 10)
        estado_jogo['marcador'].dot(2,'blue')
        update_board(estado_jogo)


def atualiza_mapa(estado_jogo, x, y, elemento):
    index = offset((x,y))
    while estado_jogo['mapa'][index] in [BLINKY_OBJECT, PINKY_OBJECT, INKY_OBJECT, CLYDE_OBJECT]:
        index += 1
    estado_jogo['mapa'][index] = elemento

def actualiza_posicao_pacman_fantasma(estado_jogo):
    x = estado_jogo['pacman']['objeto'].xcor() 
    y = estado_jogo['pacman']['objeto'].ycor()
    atualiza_mapa(estado_jogo, x, y, PACMAN_OBJECT)
    for ghost_id, ghost in estado_jogo['fantasmas'].items():
        x = ghost['objeto'].xcor()
        y = ghost['objeto'].ycor()
        atualiza_mapa(estado_jogo, x, y, ghost_id)


def guarda_jogo(estado_jogo):
    actualiza_posicao_pacman_fantasma(estado_jogo)
    str_mapa = ''
    pass

###########################################################################################################################################

def carrega_jogo(estado_jogo, nome_ficheiro):
    # Abrir e ler
    with open(nome_ficheiro, "r") as file:
        mapa = []
    
    # Processar cada linha do ficheiro
        for line in file:
        # Remover espaços em branco e vírgulas manhosas do final da linha
            line = line.strip().rstrip(",")
        
        # Adiciona nº à lista e converte para int
            mapa.extend([int(num) for num in line.split(",")])        
        

# Imprimir lista (Teste)
    print(mapa)
    
    estado_jogo['mapa'] = mapa

###########################################################################################################################################

if __name__ == '__main__':
    funcoes_jogador = {'pacman_cima': pacman_cima, 'pacman_baixo': pacman_baixo, 'pacman_esquerda': pacman_esquerda, 'pacman_direita': pacman_direita, 'guarda_jogo' : guarda_jogo, 'carrega_jogo' : carrega_jogo}    
    funcoes_fantasmas = {BLINKY_OBJECT : movimenta_blinky, PINKY_OBJECT : movimenta_pinky, INKY_OBJECT : movimenta_inky, CLYDE_OBJECT : movimenta_clyde}


    nome_ficheiro = input('Pretende carregar um mapa (Enter para carregar o mapa default): ')
    if nome_ficheiro == '':
        nome_ficheiro = 'mapa_inicial.txt'
    ##dicionario com as funcoes de movimento dos jogadores
    
    #funções de inicio do jogo
    estado_jogo = init_state()
    carrega_jogo(estado_jogo, nome_ficheiro)    
    setup(estado_jogo, True, funcoes_jogador,funcoes_fantasmas)
    
    #inicia_jogo(estado_jogo)
    while not perdeu_jogo(estado_jogo):
        if estado_jogo['mapa'] is not None:
            estado_jogo['janela'].update() #actualiza a janela
            movimenta_objectos(estado_jogo)
            atualiza_pontos(estado_jogo)
            time.sleep(0.05)