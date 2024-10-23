import pygame
from config import tela, verde, largura_tela, altura_tela, random
import time

# pygame.init()

# Configurações dos canos
largura_cano = 50
altura_cano = random.randint(100, 400)
espaco_cano = 100
cano_x = largura_tela


def desenhar_cano():
    global cano_x, altura_cano
    pygame.draw.rect(tela, verde, [cano_x, 0, largura_cano, altura_cano])
    pygame.draw.rect(
        tela, verde, [cano_x, altura_cano + espaco_cano, largura_cano, altura_tela])


def mover_cano():
    global cano_x, altura_cano
    cano_x -= 5
    if cano_x < -largura_cano:
        cano_x = largura_tela
        altura_cano = random.randint(100, 400)
        return True
    return False

# time.sleep(5)
# pygame.quit()
