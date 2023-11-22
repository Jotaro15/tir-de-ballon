import pygame
import random

from pygame.locals import *
from constante import *
from classes import *
import time
pygame.init()

mf = pygame.display.set_mode((taille_fenetre, taille_fenetre))
pygame.display.set_caption(titre_fenetre)

viseur  = pygame.image.load(image_viseur).convert_alpha()
viseur2 = pygame.image.load(image_viseur2).convert_alpha()
impact  = pygame.image.load(image_impact).convert_alpha()
fond    = pygame.image.load(image_fond).convert()
ballon  = pygame.image.load(image_ballon).convert_alpha()
ballon2 = pygame.image.load(image_ballon2).convert_alpha()

GUN = pygame.mixer.Sound(son_gun)

font = 'segoeprb.ttf'
ma_font = pygame.font.Font(font,50)


continuer = 1
ok_trace = 0
trace = Impact(mf,impact)
indic  = 0
indic0 = ''
indic1 = ''
indic2 = ''
indic3 = ''
indic4 = ''

win = 0
explose = 0
indic_explose = 0
xballon = random.randint(0,taille_fenetre - taille_ballon)
yballon = random.randint(0,taille_fenetre - taille_ballon)
xviseur = largeur / 2
yviseur = hauteur / 2
indic_feu = 0
while continuer:
    continuer_jeu = 1
    t1 = time.time()
    time.sleep(1)
    t1 += 60
    win = 0
    
    while continuer_jeu:
        t2 = round(t1 - time.time())
        compte_rebours = ma_font.render(str(t2),100,(255,255,255))
        
        indic_feu += 1
        if indic_feu >= 5:
            viseur  = pygame.image.load(image_viseur).convert_alpha()
        ballon  = pygame.image.load(image_ballon).convert_alpha()
        mf.fill(blanc)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    indic1 = 'up'
                if event.key == K_DOWN:
                    indic2 = 'down'
                if event.key == K_LEFT:
                    indic3 = 'left'
                if event.key == K_RIGHT:
                    indic4 = 'right'
                if event.key == K_SPACE:
                    GUN.play()
                    viseur = viseur2
                    trace.enregistrer(x_centre_viseur,y_centre_viseur)
                    indic_feu = 1
                    
                if event.key == K_ESCAPE:
                    continuer_jeu = 0
                    continuer = 0
            if event.type == KEYUP:
                if event.key == K_UP:
                    indic1 = ''
                if event.key == K_DOWN:
                    indic2 = ''
                if event.key == K_LEFT:
                    indic3 = ''
                if event.key == K_RIGHT:
                    indic4 = ''
        
                    
        if indic1 == 'up':
            yviseur -= 5
        if indic2 == 'down':
            yviseur += 5
        if indic3 == 'left':
            xviseur -= 5
        if indic4 == 'right':
            xviseur += 5
        
        x_centre_viseur = xviseur + 45
        y_centre_viseur = yviseur + 45

        if indic_feu == 1:
            ok_trace = 1        
            if xballon < x_centre_viseur < xballon + (taille_ballon - 25) and yballon < y_centre_viseur < yballon + (taille_ballon) :
                explose = 1
                
                
        mf.blit(fond,(0,0))
        
        if ok_trace == 1:
            trace.afficher(x_centre_viseur,y_centre_viseur)
        if explose == 1:
            mf.blit(ballon2,(xballon,yballon))
            pygame.display.flip()
            pygame.time.delay(500)
            xballon = random.randint(0,taille_fenetre - taille_ballon)
            yballon = random.randint(0,taille_fenetre - taille_ballon)
            explose = 0
            win += 1
            
        if t2 == 0.0:
            continuer_win = 1
            continuer_jeu = 0
            
        mon_text_score = ma_font.render('Score :',100,(255,255,255))
        mon_score      = ma_font.render(str(win),100,(255,0,0))
        
        mf.blit(ballon,(xballon,yballon))   
        mf.blit(viseur,(xviseur,yviseur))
        mf.blit(compte_rebours,(0,0))
        mf.blit(mon_text_score,(350,0))
        mf.blit(mon_score,(525,0))
        pygame.display.flip()
    while continuer_win:
        mf.fill(blanc)
        text_win = ma_font.render(str(win),100,(255,0,0))
        text_win1 = ma_font.render('toucher de ballon',100,(0,0,0))
        mf.blit(text_win,(0,0))
        mf.blit(text_win1,(75,0))
        pygame.display.flip()
        pygame.time.delay(1000)
        continuer_jeu = 1
        continuer_win = 0

        
