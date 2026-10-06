import pygame
import sys

#inicie o pygame 
pygame.init()

#configurações da janela do jogo 
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Jogo")

#controlar o limite de fps 
relogio = pygame.time.Clock()
#cores (RGB)
branco = (255, 255, 255)
preto = (22, 50, 80)
azul = (0, 0, 255)

#posição inicial do objetivo 
x_objetivo = 100
y_objetivo = 100
velocidade_objetivo = 5
#game loop principal
while True:
    #verifica eventos do jogo 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #movimento do objetivo 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_objetivo -= velocidade_objetivo
    if keys[pygame.K_RIGHT]:
        x_objetivo += velocidade_objetivo
    if keys[pygame.K_UP]:
        y_objetivo -= velocidade_objetivo
    if keys[pygame.K_DOWN]:
        y_objetivo += velocidade_objetivo

    #preenche a tela com a cor de fundo 
    tela.fill(preto)

    #desenha o objetivo na tela 
    pygame.draw.rect(tela, azul, (x_objetivo, y_objetivo, 50, 50))

    #atualiza a tela 
    pygame.display.flip()

    #controla o limite de fps 
    relogio.tick(60)
    #encerera o pygame
    pygame.quit()
    sys.exit()