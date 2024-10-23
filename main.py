import pygame
import random
# Certifique-se de que você está importando a função corretamente
from bird import desenhar_passaro

# Inicializa o Pygame
pygame.init()


# Configurações da tela
largura_tela = 400
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))


# Cores
azul = (135, 206, 235)
verde = (15, 255, 0)
preto = (0, 0, 0)

# Configurações do pássaro
passaro_x = 50
passaro_y = altura_tela // 2
velocidade_y = 0
gravidade = 0.5

# Configurações dos canos
largura_cano = 70
altura_cano = random.randint(100, 400)
espaco_cano = 150
cano_x = largura_tela

# Pontuação
pontos = 0
fonte = pygame.font.SysFont('Arial', 30)

# Função para desenhar os canos


def desenhar_cano(x, altura):
    pygame.draw.rect(tela, verde, [x, 0, largura_cano, altura])
    pygame.draw.rect(
        tela, verde, [x, altura + espaco_cano, largura_cano, altura_tela])


def desenhar_passaro(tela, x, y):
    cor_passaro = (255, 255, 0)  # Cor do pássaro (amarelo)
    largura_passaro = 30
    altura_passaro = 30
    pygame.draw.rect(tela, cor_passaro, [
                     x, y, largura_passaro, altura_passaro])


# No loop principal
desenhar_passaro(tela, passaro_x, passaro_y)


# Função para mostrar a tela inicial


def tela_inicial():
    tela.fill(azul)
    fonte_titulo = pygame.font.SysFont('Arial', 50)
    texto_titulo = fonte_titulo.render('Flappy Bird', True, preto)
    texto_instrucoes = fonte.render(
        'Pressione ESPAÇO para começar', True, preto)
    tela.blit(texto_titulo, (largura_tela // 4, altura_tela // 4))
    tela.blit(texto_instrucoes, (largura_tela // 6, altura_tela // 2))
    pygame.display.flip()


# Loop principal do jogo
rodando = True
jogo_ativo = False

# Tela inicial
tela_inicial()

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                if not jogo_ativo:
                    jogo_ativo = True
                    # Reiniciar variáveis para o jogo
                    passaro_y = altura_tela // 2
                    velocidade_y = 0
                    cano_x = largura_tela
                    altura_cano = random.randint(100, 400)
                    pontos = 0
                else:
                    velocidade_y = -10

    if jogo_ativo:
        # Lógica do jogo
        velocidade_y += gravidade
        passaro_y += velocidade_y

        # Atualiza a posição dos canos
        cano_x -= 5
        if cano_x < -largura_cano:
            cano_x = largura_tela
            altura_cano = random.randint(100, 400)
            pontos += 1

        # Verifica colisões
        if (passaro_y > altura_tela or passaro_y < 0 or
                (cano_x < passaro_x + 30 < cano_x + largura_cano and
                 (passaro_y < altura_cano or passaro_y + 30 > altura_cano + espaco_cano))):
            jogo_ativo = False  # Finaliza o jogo

        # Atualiza a tela
        tela.fill(azul)

        # Desenha o pássaro
        desenhar_passaro(tela, passaro_x, passaro_y)

        # Desenha os canos
        desenhar_cano(cano_x, altura_cano)

        # Exibe a pontuação
        texto_pontos = fonte.render(f'Pontuação: {pontos}', True, preto)
        tela.blit(texto_pontos, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
