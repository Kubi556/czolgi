from json import load
from turtle import speed
import pygame
from random import random
import time
import sys, pygame, pygame.mixer
from pygame.locals import * 
import math
import sys, pygame, pygame.mixer
from pygame.locals import * 
from random import random
import math


# uruchomienie biblioteki pygame
pygame.init()

#zegar
clock = pygame.time.Clock()

#pociski
pociski = []
  
# zdefiniowane kolory
white = (255, 255, 255)
rosso=(255,0,0)
green = (0, 255, 0)
skyblue = (0,191,255)
black =(1,1,1)
# rozmiar okna
X = 1200
Y = 700
kierunek_czolgu = True #True dla prawo False dla lewo



# stworzenie okna o wymiarach X, Y
display_surface = pygame.display.set_mode((X, Y ))
  
# ustawienie nazwy okna modułu pygame
pygame.display.set_caption('Image')
  
# stworzenie obiektu na płaszczyźnie okna
tank = pygame.image.load(r'C:\Users\rober\Desktop\workspace\gry\czolgi\grafika\tank.png').convert_alpha()   #przypisanie zmiennej tank zdjecia
tank = pygame.transform.scale(tank, (65, 40))  #zmiana rozmiaru zdjecia do 40 na 30 pikseli
pocisk = pygame.draw.circle(display_surface, rosso, (100,100), 20)
strzal = pygame.mixer.Sound('gry\czolgi\sf_cannon_01.mp3')

#czolg przeciwnika
enemy_tank = pygame.image.load(r'C:\Users\rober\Desktop\workspace\gry\czolgi\grafika\tank.png').convert_alpha()   #przypisanie zmiennej tank zdjecia
enemy_tank = pygame.transform.scale(enemy_tank, (65, 40))
enemy_tank = pygame.transform.flip(enemy_tank, True, False)


#zmienne mówiące o początkowej pozycji czołgu
minx = 20
maxx = 340
losowa = minx + (random() * (maxx - minx))

nachylenie = 0

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Kąt nachylenia: {}'.format(nachylenie), True, (111,111, 111))

tank_pos_x = losowa
tank_pos_y = 559

#zmienne mówiące o początkowej pozycji czołgu
enemy_minx = 1280
enemy_maxx = 520 #940 dla full HD
#formula na losowa liczbe miedzy min a max:
enemy_losowa = enemy_minx + (random() * (enemy_maxx - enemy_minx))
etank_pos_x = enemy_losowa 
etank_pos_y = 559


#stałe dt. pocisku
ball={'m': 1, 'v':[0,0], 'pos':{'x': losowa, 'y':390}}
g=-9.8
v0=8
theta=nachylenie*3.14158/180        #masa kuli
ball['v']=[v0*math.cos(theta),v0*math.sin(theta)]    #wektor prędkości kuli
t=0
dt=0.01

#funkcje

def narysujOknoGry():
    display_surface.fill(white)
    pygame.draw.rect(display_surface,green,[00,410,800,100]) #rysowanie tła
    display_surface.blit(tank, (tank_pos_x, tank_pos_y))
    display_surface.blit(textsurface, (40, 50))
    display_surface.blit(enemy_tank, (etank_pos_x, etank_pos_y))
    
    clock.tick(60)
    pygame.display.update()
    
# niekończąca się pętla
while True :
    
    # wypełnienie okna kolorem niebieskim
    display_surface.fill(skyblue)

    display_surface.blit(enemy_tank, (etank_pos_x, etank_pos_y))
    display_surface.blit(textsurface, (40, 50))

    display_surface.blit(tank, (tank_pos_x, tank_pos_y))
    display_surface.blit(textsurface, (40, 50))
    # kopiowanie obiektu do płaszczyzny na pozycję

    #(tank_pos_x, tank_pos_y)
    #display_surface.blit(tank, (tank_pos_x, tank_pos_y))
    pygame.draw.rect(display_surface,green,[00,600,1200,100])

    # pętla przez zdarzenia (np naciśnięcie klawisza)
    for event in pygame.event.get() :
        
        if event.type == pygame.KEYDOWN: #nasłuchiwanie klawiszy
            
            if event.key == pygame.K_SPACE: #jeśli spacja naciśnięta to:
                print("BOOM!")
                strzal.play()
                while ball['pos']['y']>=380:
                    F=ball['m']*g
                    ball['v'][1]=ball['v'][1]-(F/ball['m'])*dt
                    ball['pos']['x']=ball['pos']['x']+ball['v'][0]*dt/ball['m']
                    ball['pos']['y']=ball['pos']['y']-ball['v'][1]*dt/ball['m']
                    t=t+dt
                    print(ball)
                    display_surface.blit(pocisk, (ball['pos']['x'], ball['pos']['y']))
                #pociski.append([losowa+10, 390])
                print("Pociski =",pociski[0][0], pociski[0][1])
                display_surface.blit(pocisk, (pociski[0][0], pociski[0][1]))
                pygame.draw.rect(display_surface,rosso,[100,100,100,100])
            
            if event.key == pygame.K_UP:
                if nachylenie == 90:
                    print("Osiągnęto maksymalne nachylenie!")
                else:
                    nachylenie += predkosc
                    if nachylenie > 90: #w razie przekroczenia 180 stopni
                        nachylenie = 90
                    predkosc *= 4
                    textsurface = myfont.render('Kąt nachylenia: {}'.format(nachylenie), True, (111,111, 111))

            if event.key == pygame.K_UP and event.key == pygame.K_LSHIFT:
                print("UP")
                nachylenie += 10
                textsurface = myfont.render('Kąt nachylenia: {}'.format(nachylenie), True, (111,111, 111))    
            
            if event.key == pygame.K_DOWN:
                nachylenie += -1
                textsurface = myfont.render('Kąt nachylenia: {}'.format(nachylenie), True, (111,111, 111))
            
            if event.key == pygame.K_LEFT:
                if kierunek_czolgu == True:
                   tank = pygame.transform.flip(tank, True, False)
                   kierunek_czolgu = False
                   #display_surface.blit(tank, (tank_pos_x, tank_pos_y))
                print("LEFT")
                tank_pos_x+=-7
           
            if event.key == pygame.K_RIGHT:
                if kierunek_czolgu == False:
                   tank = pygame.transform.flip(tank, True, False)
                   kierunek_czolgu = True
                   #display_surface.blit(tank, (tank_pos_x, tank_pos_y))
                print("RIGHT")
                tank_pos_x+=7

            if nachylenie >- 13:    #zmiany pozycji(trzeba mieć gotowe obrazki)
                tank = pygame.image.load(r'C:\Users\rober\Desktop\workspace\gry\czolgi\grafika\tank.png')
                tank = pygame.transform.scale(tank, (65, 40))
                if kierunek_czolgu == False:
                    tank = pygame.transform.flip(tank, True, False)
                    #display_surface.blit(tank, (tank_pos_x, tank_pos_y))

            if nachylenie > 14:
                tank = pygame.image.load(r'C:\Users\rober\Desktop\workspace\gry\czolgi\grafika\tank2.png')
                tank = pygame.transform.scale(tank, (65, 40))    
                if kierunek_czolgu == False:
                    tank = pygame.transform.flip(tank, True, False)
                    #display_surface.blit(tank, (tank_pos_x, tank_pos_y))

            if nachylenie > 29:
                tank = pygame.image.load(r'C:\Users\rober\Desktop\workspace\gry\czolgi\grafika\tank3.png')
                tank = pygame.transform.scale(tank, (65, 40))        
                if kierunek_czolgu == False:
                    tank = pygame.transform.flip(tank, True, False)
                    #display_surface.blit(tank, (tank_pos_x, tank_pos_y))

            if nachylenie > 44:
                tank = pygame.image.load(r'C:\Users\rober\Desktop\workspace\gry\czolgigrafika\tank4.png')
                tank = pygame.transform.scale(tank, (65, 40))
                if kierunek_czolgu == False:
                    tank = pygame.transform.flip(tank, True, False)
                    #display_surface.blit(tank, (tank_pos_x, tank_pos_y))
                    
            if nachylenie <- 14:
                tank = pygame.image.load(r'C:\Users\rober\Desktop\workspace\gry\czolgi\grafika\tank1.png')
                tank = pygame.transform.scale(tank, (65, 40))               
                if kierunek_czolgu == False:
                    tank = pygame.transform.flip(tank, True, False)
                    #display_surface.blit(tank, (tank_pos_x, tank_pos_y))

            

            
            if nachylenie > 90:
                nachylenie = -1
            if nachylenie <- 30:
                nachylenie = 1
            if event.key == pygame.K_ESCAPE:
                pygame.quit
                quit()
            # odłączenie biblioteki pygam
  
            # wyjście z programu
                      


        #time.sleep(1)    #opuźnienie 1 sekunda
        #ustawienie zegara
        clock = pygame.time.Clock()
        clock.tick(175) 
        # rysowanie obiektów na ekranie
        pygame.display.update()