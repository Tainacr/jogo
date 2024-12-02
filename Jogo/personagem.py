import pygame

class Personagem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y
        self.velocidade = 6
        self.gravidade = 0.5
        self.velocidade_y = 0
        self.no_chao = True

        # Sprites do personagem
        self.sprite_parado = pygame.image.load('assets/parado.png').convert_alpha()
        self.sprite_andando1 = pygame.image.load('assets/andando1.png').convert_alpha()
        self.sprite_andando2 = pygame.image.load('assets/andando2.png').convert_alpha()
        self.sprite_pulando = pygame.image.load('assets/pulando.png').convert_alpha()

        # Redimensionar sprites
        self.sprite_parado = pygame.transform.scale(self.sprite_parado, (100, 100))
        self.sprite_andando1 = pygame.transform.scale(self.sprite_andando1, (100, 100))
        self.sprite_andando2 = pygame.transform.scale(self.sprite_andando2, (100, 100))
        self.sprite_pulando = pygame.transform.scale(self.sprite_pulando, (100, 100))

        # Configuração inicial
        self.image = self.sprite_parado
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        # Controle de movimento
        self.movendo = False
        self.frame_andando = 0
        self.delay_andando = 10
        self.tempo_andando = 0

    def atualizar(self, teclas):
        self.movendo = False

        # Movimentação horizontal
        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidade
            self.movendo = True
        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidade
            self.movendo = True

        # Pulo
        if teclas[pygame.K_SPACE] and self.no_chao:
            self.velocidade_y = -10
            self.no_chao = False

        # Aplicar gravidade
        self.velocidade_y += self.gravidade
        self.y += self.velocidade_y

        # Limitar ao chão
        if self.y >= 400:
            self.y = 400
            self.velocidade_y = 0
            self.no_chao = True

        # Animações
        if not self.no_chao:
            self.image = self.sprite_pulando  # Mostra o sprite de pulo
        elif self.movendo:
            if self.tempo_andando >= self.delay_andando:
                if self.frame_andando % 2 == 0:
                    self.image = self.sprite_andando1
                else:
                    self.image = self.sprite_andando2
                self.frame_andando += 1
                self.tempo_andando = 0
            self.tempo_andando += 1
        else:
            self.image = self.sprite_parado

        # Atualizar posição
        self.rect.center = (self.x, self.y)

    def desenhar(self, tela):
        tela.blit(self.image, self.rect)
