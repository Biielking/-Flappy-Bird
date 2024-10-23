import pygame

# Cores e variáveis usadas no desenho
preto = (0, 0, 0)
largura_passaro = 25
altura_passaro = 25

# Função para desenhar o pássaro


def desenhar_passaro(tela, passaro_x, passaro_y):
    pygame.draw.rect(
        tela, preto, [passaro_x, passaro_y, largura_passaro, altura_passaro])
