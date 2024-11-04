# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from random import *
from pygame.sprite import Group

pygame.init()

# ----- Gera tela principal
WIDTH = 1080
HEIGHT = 720

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('jogo do pato')
macaco_img = pygame.image.load('assets/img/macaco.png').convert_alpha()
assets={}
fonte=pygame.font.get_default_font()
assets['fonte']=pygame.font.Font(fonte,28)
assets['pontos']=0


# ----- Inicia estruturas de dados
# Definindo os novos tipos
class Monkey (pygame.sprite.Sprite):
    def __init__(self):
        # adicionamacaco
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets\img\macaco.png")
        self.image = pygame.transform.scale(self.image,(150,150))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

class Pato(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("assets\img\WIN_20240909_16_24_05_Pro.jpg")
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        # self.rect.x=randint(1070,1080)
        # self.rect.y=randint(0,720)
        # self.speedx=randint(-5,-3)
        # self.speedy=randint(-1,-1)
        if randint(1, 2) == 1:
            # Lado direito
            self.rect.x = randint(1070, 1080)
            self.speedx = randint(-5, -3)
        else:
            # Lado esquerdo
            self.rect.x = randint(10, 60)
            self.speedx = randint(3, 5)
        
        self.rect.y = randint(0, 720)
        self.speedy = randint(-1, 1)  

#atualiza as posicoes e tudo
    def update(self):
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy

        if self.rect.x<=0 or self.rect.y<=0 or self.rect.x>1080 or self.rect.y>720:
            if randint(1, 2) == 1:
            # Lado direito
                self.rect.x = randint(1070, 1080)
                self.speedx = randint(-5, -3)
            else:
            # Lado esquerdo
                self.rect.x = randint(10,60)
                self.speedx = randint(3, 5)
            
            self.rect.y = randint(0, 720)
            self.speedy = randint(-1, 1)  

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
clock = pygame.time.Clock()
FPS = 60
image = pygame.image.load('assets/img/fundo.jpg').convert() 
image = pygame.transform.scale(image,(1080,720)) 
all_sprites = pygame.sprite.Group()
all_sprites.add(Monkey())
#criando patos
for i in range(15):
    patinhos = Pato()
    all_sprites.add(patinhos)

# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type ==pygame.MOUSEBUTTONDOWN:
            for pato in all_sprites:
                if pato.rect.x<=event.pos[0]<=pato.rect.x+50 and pato.rect.y<=event.pos[1]<=pato.rect.y+50:
                    assets['pontos'] += 1
                    pato.rect.x =-100
                    pato.rect.y =-100
    # ----- Gera saídas
    text_surface = assets['fonte'].render(f"{assets['pontos']}", True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  10)
    all_sprites.update()
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image, (0, 0))
    all_sprites.draw(window)
    window.blit(text_surface, text_rect)


    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
