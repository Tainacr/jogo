import pygame

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.velocidade = 3

        # Sprites do inimigo
        self.sprite_andando1 = pygame.image.load('assets/enemy_andando1.png').convert_alpha()
        self.sprite_andando2 = pygame.image.load('assets/enemy_andando2.png').convert_alpha()
        self.sprite_ataque = pygame.image.load('assets/enemy_ataque.png').convert_alpha()

        # Redimensionar sprites
        self.sprite_andando1 = pygame.transform.scale(self.sprite_andando1, (100, 100))
        self.sprite_andando2 = pygame.transform.scale(self.sprite_andando2, (100, 100))
        self.sprite_ataque = pygame.transform.scale(self.sprite_ataque, (100, 100))

        self.image = self.sprite_andando1
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        # Controle de movimento e animação
        self.frame_andando = 0
        self.delay_andando = 10
        self.tempo_andando = 0
        self.atacando = False
        self.tempo_ataque = 0
        self.delay_ataque = 60  # Delay entre ataques (em frames)

    def atualizar(self, personagem, grupo_dinheiro):
        self.atacando = False

        # Movimento do inimigo
        self.rect.x -= self.velocidade

        # Alternar sprites de movimento
        if self.tempo_andando >= self.delay_andando:
            if self.frame_andando % 2 == 0:
                self.image = self.sprite_andando1
            else:
                self.image = self.sprite_andando2
            self.frame_andando += 1
            self.tempo_andando = 0
        self.tempo_andando += 1

        # Ataque
        if abs(self.rect.centerx - personagem.rect.centerx) < 150:
            if self.tempo_ataque >= self.delay_ataque:
                self.atacando = True
                self.image = self.sprite_ataque
                self.arremessar_dinheiro(personagem, grupo_dinheiro)
                self.tempo_ataque = 0
        self.tempo_ataque += 1

    def arremessar_dinheiro(self, personagem, grupo_dinheiro):
        dinheiro = Dinheiro(self.rect.centerx, self.rect.centery, personagem)
        grupo_dinheiro.add(dinheiro)


class Dinheiro(pygame.sprite.Sprite):
    def __init__(self, x, y, personagem):
        super().__init__()
        self.image = pygame.image.load('assets/dinheiro.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidade_x = -5 if x > personagem.rect.x else 5
        self.velocidade_y = -3

    def update(self):
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y
