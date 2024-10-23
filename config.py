import pygame
import random
import time

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura_tela = 720
altura_tela = 1280
tela = pygame.display.set_mode((largura_tela, altura_tela))


# Cores
branco = (255, 255, 255)
verde = (50, 255, 0)
preto = (0, 0, 0)

# Pontuação
pontos = 0
fonte = pygame.font.SysFont('Arial', 30)

# Gravidade
gravidade = 0.05

# time.sleep(5)

# pygame.quit()
