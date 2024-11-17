# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from random import *
from pygame.sprite import Group
import os
from os import path

img_dir = os.path.join(os.path.dirname(_file_), 'assest', 'img')

def load_spriteshhet(spritesheet,rows,columns):
    sprite_width=spritesheet.get_width()//columns
    sprite_height=spritesheet.get_height()//rows
    sprites=[]
    for row in range(rows):
        for column in range(columns):
            x= column* sprite_width
            y= row * sprite_height
            image = pygame.Surface((sprite_width,sprite_height),pygame.SRCALPHA)
            image.blit(spritesheet,(0,0),pygame.Rect(x,y,sprite_width,sprite_height))
            sprites.append(image)
    return sprites
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
game_over_image = pygame.image.load('assets/img/game_over.webp')
game_over_image = pygame.transform.scale(game_over_image, (1080, 720)) 
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
    def _init_(self):
        # adicionamacaco
        pygame.sprite.Sprite._init_(self)
        self.image = pygame.image.load("assets/img/macaco.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
class Pato(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
        super()._init_()
        self.spritesheet = pygame.image.load(path.join('assets\img\hoho.png')).convert_alpha()
        self.spritesheet = pygame.transform.scale(self.spritesheet, (1000,1000))
        self.sprites = load_spriteshhet(self.spritesheet,3,5)
        self.animations= {
            'left':self.sprites[0:2],
            'stay_left': self.sprites[0]
        }
        self.state='stay_left'
        self.animation = self.animations[self.state]
        self.frame=0
        self.sprite_speed=0
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 300
        self.image = self.animation if isinstance(self.animation,list) else self.animation
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
        self.state='left'
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.x <= 0 or self.rect.y <= 0 or self.rect.x > 1080 or self.rect.y > 720:
            if randint(1, 2) == 1:
            # Lado direito
                self.rect.x = randint(1070, 1080)
                self.speedx = randint(-5, -3)
            else:
            # Lado esquerdo
                self.sprite_speed=5
                self.rect.x = randint(10,60)
                self.speedx = randint(3, 5)
            
            self.rect.y = randint(0, 720)
            self.speedy = randint(-1, 1)  
        if self.sprite_speed!=0:
            self.animate()
    def animate(self):
        now=pygame.time.get_ticks()
        elapsed_ticks=now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            self.last_update=now
            self.frame+=1
            if self.frame>=len(self.animations[self.state]):
                self.frame=0
        center= self.rect.center
        self.image=self.animations[self.state][self.frame]
        self.rect=self.image.get_rect()
        self.rect.center=center
class PatoFAST(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
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
                for Pato in all_sprites:  # Itera sobre todos os sprites
        # Verifica se o clique está dentro do retângulo do sprite
                    if (Pato.rect.x <= event.pos[0] <= Pato.rect.x + Pato.rect.width and Pato.rect.y <= event.pos[1] <= Pato.rect.y + Pato.rect.height):
            # Adiciona pontos (diferente para Pato e PatoFAST)
                        assets['pontos'] += 1  # A pontuação é definida na classe
                        
                        Pato.rect.x = -100
                        Pato.rect.y = -100

                for PatoFAST in all_sprites:
                    if PatoFAST.rect.x <= event.pos[0] <= PatoFAST.rect.x+50 and PatoFAST.rect.y <= event.pos[1] <= PatoFAST.rect.y+50:
                         assets['pontos'] += 3
                         PatoFAST.rect.x =-100
                         PatoFAST.rect.y =-100
                        
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
    
        assets['tempo_inicial'] += (clock.get_time()/1000)
        

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game ='inicio'
                    assets['pontos'] = 0  # Reseta os pontos apenas ao reiniciar o jogo
                    assets['tempo'] = 0
        window.fill((0, 0, 0))  # Fundo preto
        window.blit(game_over_image, ((WIDTH - game_over_image.get_width()) // 2, (HEIGHT - game_over_image.get_height()) // 2))  # Centraliza a imagem
        texto_pontuacao_final = assets['fonte'].render(f"SCORE: {assets['pontos']}", True, (255, 255, 255))
        texto_pontuacao_final_rect = texto_pontuacao_final.get_rect()
        texto_pontuacao_final_rect.center = (WIDTH // 2, HEIGHT // 2 + 250)  # Ajuste a posição conforme necessário
        pygame.draw.rect(window, (0, 0, 0), texto_pontuacao_final_rect) # Desenha o retângulo preto

    # Renderiza o texto da pontuação final por cima do retângulo
    
        window.blit(texto_pontuacao_final, texto_pontuacao_final_rect)
        pygame.display.update()
        
# ===== Finalização =====

pygame.quit()  # Função do PyGame que finaliza os recursos utilizados