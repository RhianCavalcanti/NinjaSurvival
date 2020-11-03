import pygame
from random import randint
from pygame.locals import*
try:

    pygame.init()

except:
    print("Erro na inicializaçao do pygame.init()")

largura = 925
altura = 720

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Ninja Survival")

clock = pygame.time.Clock()
pygame.mixer.music.load('narutost.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
movikunai = pygame.image.load("Kunaiesq.png")


andardir = [
    pygame.image.load("Player movimentos/Rundir0.png"),
    pygame.image.load("Player movimentos/Rundir1.png"),
    pygame.image.load("Player movimentos/Rundir2.png"),
    pygame.image.load("Player movimentos/Rundir3.png"),
    pygame.image.load("Player movimentos/Rundir4.png"),
    pygame.image.load("Player movimentos/Rundir5.png"),
    pygame.image.load("Player movimentos/parado.png"),
]

andaresq = [
    pygame.image.load("Player movimentos/Runesq0.png"),
    pygame.image.load("Player movimentos/Runesq1.png"),
    pygame.image.load("Player movimentos/Runesq2.png"),
    pygame.image.load("Player movimentos/Runesq3.png"),
    pygame.image.load("Player movimentos/Runesq4.png"),
    pygame.image.load("Player movimentos/Runesq5.png"),
    pygame.image.load("Player movimentos/parado.png"),
]

print(andaresq[-5].get_rect())
bg = pygame.image.load("BG.png")


class player(object):
    def __init__(self, x, y, largurap, alturap):
        self.x = x
        self.y = y
        self.largurap = largurap
        self.alturap = alturap
        self.vel = 15
        self.pulo = False
        self.contpulo = 10
        self.esq = False
        self.dir = False
        self.contpasso = 0

d=0
def jogo():
    janela.blit(bg, (0, 0))


    if player.contpasso + 1 >= 12:
        player.contpasso = 0
    if player.esq:
        janela.blit(andaresq[player.contpasso // 3], (player.x, player.y))
        player.contpasso += 1
    elif player.dir:
        janela.blit(andardir[player.contpasso // 3], (player.x, player.y))
        player.contpasso += 1
    else:
        janela.blit(andardir[-1], (player.x, player.y))
    #movimento das kunais
    janela.blit(movikunai, (pos_x, pos_y))
    janela.blit(texto,pos_texto)
    pygame.display.update()




velocidade_outros = 12

d = 0
pos_x = 925
pos_y = 535
player = player(200, 500, 91, 115)  # peguei a largura e altura(91,115) usando o get_rect
score= 0
temposeg=0
loop = True
vida=1
gameoverv=1
som=1
while loop:
    clock.tick(60)
    keys = pygame.key.get_pressed()
   #rect de colisao
    playerrect = (player.x,player.y,player.largurap, player.alturap)
    kunairect=pygame.draw.rect(janela,(0,0,0), [pos_x,pos_y, 25,5])
    gameover= pygame.image.load("telagameover.png")
    #score do jogo
    font = pygame.font.SysFont('arial black', 30)
    texto = font.render("Score: ", True, (255, 255, 255), (0, 0, 0))
    pos_texto = texto.get_rect()
    pos_texto.center = (100, 50)
    somdano= pygame.mixer.Sound("somdano2.ogg")
    print(somdano.get_num_channels())
    if pos_x>0:
        pos_x -= velocidade_outros+1
    else:
        pos_x= randint(925,1500)
    #condicionais para quando o player for atigindo pela kunai efutar colisao, som, tela gameover e parar o score
    if kunairect.colliderect(playerrect):
        vida=0
        som=0
        gameoverv=0
    if vida == 0 and som==0:
        somdano.play(0)
        som+=1
    else:
        somdano.stop()

    if (score < 20):
        score += 2
    else:
        if  vida!=0:
            temposeg += 1
            texto = font.render("Score: " + str(temposeg), True, (255, 255, 255), (0, 0, 0))
            score = 0
        if vida==0:
            temposeg = temposeg
            texto = font.render("Score: " + str(temposeg), True, (255, 255, 255), (0, 0, 0))
            score = 0

    if gameoverv == 0:
        janela.blit(gameover, (155, 70))  # fiz outra condicional para a 'colisaotela' aparecer e não sair
        pygame.mixer.music.stop()



    if keys[pygame.K_a] and player.x > 10:
        player.x -= player.vel
        player.dir = False
        player.esq = True

    elif keys[pygame.K_d] and player.x < 925 - player.largurap - player.vel:
        player.x += player.vel
        player.dir = True
        player.esq = False

    else:
        player.dir = False
        player.esq = False
        player.contpasso = 0

    if not player.pulo:
        if keys[pygame.K_w]:
            player.pulo = True

    else:
        if player.contpulo >= -10:
            neg = 1
            if player.contpulo < 0:
                neg = -1

            player.y -= (player.contpulo ** 2) / 2 * neg
            player.contpulo -= 1
        else:
            player.pulo = False
            player.contpulo = 10
    if vida==0:#condicional para quando o player for atigindo não se mover
        player.pulo= False
        player.esq= False
        player.dir= False
        player.contpasso=0
        player.contpulo=0
        player.vel=0
    pygame.display.update()
    jogo()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            loop = False
