import pygame
from personagem import Personagem
from inimigo import Inimigo

# Inicializa o pygame
pygame.init()

# Configurações da tela
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Jogo Metroidvania")

# Cores
PRETO = (0, 0, 0)

# Carregar imagens das salas
sala1 = pygame.image.load('assets/sala1.png')
sala2 = pygame.image.load('assets/sala2.png')
sala3 = pygame.image.load('assets/sala3.png')

# Redimensionar o fundo para preencher a tela
sala1 = pygame.transform.scale(sala1, (LARGURA_TELA, ALTURA_TELA))
sala2 = pygame.transform.scale(sala2, (LARGURA_TELA, ALTURA_TELA))
sala3 = pygame.transform.scale(sala3, (LARGURA_TELA, ALTURA_TELA))

# Chão (diminuído)
CHAO_Y = 500  # Reduzido a altura do chão
chao = pygame.Surface((LARGURA_TELA, ALTURA_TELA - CHAO_Y))
chao.fill((139, 69, 19))  # Cor de chão (marrom)

# Criando o personagem e inimigo
personagem = Personagem(100, CHAO_Y - 100)  # Colocando o personagem em cima do chão
inimigos = pygame.sprite.Group()
grupo_dinheiro = pygame.sprite.Group()

# Adicionando inimigos
inimigo = Inimigo(700, CHAO_Y - 100)
inimigos.add(inimigo)

# Grupo de sprites
todos_sprites = pygame.sprite.Group()
todos_sprites.add(personagem)
todos_sprites.add(inimigo)

# Clock para controlar a taxa de quadros
clock = pygame.time.Clock()

# Loop principal do jogo
rodando = True
tela_atual = sala1  # Sala inicial
while rodando:
    # Controle de FPS
    clock.tick(60)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Atualizando as posições
    teclas = pygame.key.get_pressed()
    personagem.atualizar(teclas)

    # Verificando a colisão com o chão
    if personagem.rect.bottom >= CHAO_Y:
        personagem.rect.bottom = CHAO_Y
        personagem.velocidade_y = 0  # Para a gravidade ao atingir o chão
        personagem.no_chao = True
    else:
        personagem.no_chao = False

    inimigos.update(personagem, grupo_dinheiro)

    # Verificando a colisão com as bordas da tela e trocando de sala
    if personagem.rect.right >= LARGURA_TELA:
        if tela_atual == sala1:
            tela_atual = sala2
        elif tela_atual == sala2:
            tela_atual = sala3

        # Colocando o personagem no início da próxima sala
        personagem.rect.x = 100  # Resetando a posição X do personagem

    # Desenhando o fundo da sala
    tela.blit(tela_atual, (0, 0))

    # Desenhando o chão
    tela.blit(chao, (0, CHAO_Y))

    # Desenhando os inimigos e o personagem
    todos_sprites.draw(tela)

    # Atualizando a tela
    pygame.display.flip()

# Finalizando o jogo
pygame.quit()
