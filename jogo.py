# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from random import *
from pygame.sprite import Group
# Inicialize o clock no início do programa
clock = pygame.time.Clock()
FPS = 60

pygame.init()

# ----- Gera tela principal
WIDTH = 1080
HEIGHT = 720

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('jogo do pato')
macaco_img = pygame.image.load('assets/img/macaco.png').convert_alpha()
assets = {}
fonte = pygame.font.get_default_font()
fonte2 = pygame.font.match_font('arial')
assets['fonte'] = pygame.font.Font(fonte,28)
assets['fonte2'] = pygame.font.Font(fonte2,28)
assets['pontos'] = 0
assets['tempo'] = 0
assets['tempo_inicial'] = 0


# ----- Inicia estruturas de dados
# Definindo os novos tipos
class Monkey(pygame.sprite.Sprite):
    def __init__(self):
        # adicionamacaco
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/img/macaco.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
class Pato(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/img/patinhoquaqua.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        
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
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.x <= 0 or self.rect.y <= 0 or self.rect.x > 1080 or self.rect.y > 720:
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
 
class PatoFAST(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/img/patosfast.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()  # Corrige para usar self.rect
        
        if randint(1, 2) == 1:
            # Lado direito
            self.rect.x = randint(1070, 1080)
            self.speedx = randint(-7, -4)
        else:
            # Lado esquerdo
            self.rect.x = randint(10, 60)
            self.speedx = randint(4, 7)
        
        self.rect.y = randint(0, 720)
        self.speedy = randint(-1, 1)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.x <= 0 or self.rect.y <= 0 or self.rect.x > 1080 or self.rect.y > 720:
            if randint(1, 2) == 1:
                # Lado direito
                self.rect.x = randint(1070, 1080)
                self.speedx = randint(-7, -4)
            else:
                # Lado esquerdo
                self.rect.x = randint(10, 60)
                self.speedx = randint(4, 7)
            
            self.rect.y = randint(0, 720)
            self.speedy = randint(-1, 1)



# ----- Inicia estruturas de dados
game = 'inicio'

# ----- Inicia assets
image = pygame.image.load('assets/img/fundo.jpg').convert() 
image = pygame.transform.scale(image,(1080,720)) 
all_sprites = pygame.sprite.Group()
all_sprites.add(Monkey())

#criando patos
for i in range(15):
    patinhos = Pato()
    all_sprites.add(patinhos)
for i in range(5):
    patinhos = PatoFAST()
    all_sprites.add(patinhos)

# ===== Loop principal =====
while game != False:
    while game == 'jogo':
        clock.tick(FPS)
        #FUNÇAO TEMPO
        assets['tempo'] += ((clock.get_time()/1000))
        if assets['tempo'] >= 20:
            game= 'gameover'
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for Pato in all_sprites:
                    if Pato.rect.x <= event.pos[0] <= Pato.rect.x+50 and Pato.rect.y <= event.pos[1] <= Pato.rect.y+50:
                        assets['pontos'] += 1
                        Pato.rect.x =-100
                        Pato.rect.y =-100
                        
        # ----- Gera saídas
        texto_pontos = assets['fonte'].render(f"{assets['pontos']}", True, (255, 255, 0))
        if assets['tempo']>=0:
            texto_tempo = assets['fonte'].render(f"TEMPO:{assets['tempo'] :.0f}", True, (255, 255, 0))
        else:
            texto_tempo = assets['fonte'].render(f"TEMPO:0", True, (255, 255, 0))
        texto_pontos_rect = texto_pontos.get_rect()
        texto_pontos_rect.midtop = (WIDTH / 2,  10)
        texto_tempo_rect = texto_tempo.get_rect()
        texto_tempo_rect.midtop = (WIDTH -90,  10)
        all_sprites.update()
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(image, (0, 0))
        all_sprites.draw(window)
        window.blit(texto_pontos, texto_pontos_rect)
        window.blit(texto_tempo, texto_tempo_rect)
    
        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
    while game == 'inicio':
        clock.tick(FPS)
        assets['pontos'] = 0
        assets['tempo_inicial'] += (clock.get_time()/1000)
        font = pygame.font.SysFont(None, 48)
        texto_tela_inicial = assets['fonte'].render('MATA PATO', True, (0, 0, 255))
        texto_tela_inicial2 = assets['fonte'].render('Precione espaço para começar', True, (0, 0, 255))
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game ='jogo'
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(texto_tela_inicial,(WIDTH/2-40,HEIGHT/2-10))
        window.blit(texto_tela_inicial2,(WIDTH/2-40,240))
        pygame.display.update() 
         # Mostra o novo frame para o jogador
    while game == 'gameover':
        clock.tick(FPS)
        assets['pontos'] = 0
        assets['tempo'] = 0
        assets['tempo_inicial'] += (clock.get_time()/1000)
        texto_tela_final = assets['fonte2'].render('Game Over ', True, (0, 0, 0))

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game ='inicio'
        window.fill((0, 0, 255))  # Preenche com a cor branca
        window.blit(texto_tela_final,(WIDTH/2-40,HEIGHT/2-10))
        pygame.display.update()  # Mostra o novo frame para o jogador
# ===== Finalização =====

pygame.quit()  # Função do PyGame que finaliza os recursos utilizados