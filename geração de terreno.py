# Imports
import pygame, sys
from random import randint as ran

# Bloco 1
    # Classe
class Celula(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # Função
def gerarTerreno():
    # Gerando terreno aleatório
    celulaLista = []
    for x in range(colunas):
        celulaListaLinhas = []
        for y in range(linhas):
            tipoCelula = ran(0, 100)
            if tipoCelula/100 <= probAgua:
                tipoCelula = 0
            else:
                tipoCelula = 1
            celulaListaLinhas.append(tipoCelula)
        celulaLista.append(celulaListaLinhas)

    # Gerando padrões com base nas células vizinhas
    for x in range(colunas-1):
        for y in range(linhas-1):
            '''vizinhos = [
            celulaLista[x-1][y-1],
            celulaLista[x-1][y],
            celulaLista[x-1][y+1],
            celulaLista[x][y-1],
            celulaLista[x][y+1],
            celulaLista[x+1][y-1],
            celulaLista[x+1][y],
            celulaLista[x+1][y+1]]

            if vizinhos.count(1) >= 5:
                celulaLista[x][y] = 1

            if ran(0, 100)/100 <= probPolvo and celulaLista[x][y] == 0:
                celulaLista[x][y] = 2

            if ran(0, 100)/100 <= probArvore and celulaLista[x][y] == 1:
                celulaLista[x][y] = 3'''

            novaCelula = Celula(x*tamanho, y*tamanho, imgLista[celulaLista[x][y]])
            celulaGrupo.add(novaCelula)

# Bloco 2
tamanho = 16 # pixels
colunas = 40
linhas = 40
worldx, worldy = (colunas - 1) * tamanho, (linhas - 1) * tamanho
probAgua = 0.5 # porcentagem de uma célula ser água
probPolvo = 0.05
probArvore = 0.05

pygame.init()
world = pygame.display.set_mode([worldx, worldy])
pygame.display.set_caption('Geração Procedural de Terreno - Automato Celular')

imgLista = [
'Automato Celular\\agua.png',
'Automato Celular\\terra.png',
'Automato Celular\\polvo.png',
'Automato Celular\\arvore.png']

celulaGrupo = pygame.sprite.Group()

# Bloco 3
main = True
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gerarTerreno()
    world.fill((255, 255, 130))
    celulaGrupo.draw(world)
    pygame.display.flip()
