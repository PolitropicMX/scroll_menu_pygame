#ok banda hoy hare un vaso, un recipiente en python
import pygame, sys
import numpy as np
import math
from button import Button
# Initialize the pygame
pygame.init()

#Create the screen
HEIGHT, WIDTH = 600,700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pygame project")
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

#Create the clock
clock = pygame.time.Clock()

#Codeline for the image background
#background = pygame.image.load('')

font = pygame.font.Font('freesansbold.ttf',32)


# variables
segundero = 0
cur_vel_x = 0
cur_vel_y = 0
cur_x = 100
cur_y = 100
# programare visualmente el diagrama de





# Funciones de dibujo
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont("f", size)
def dot(xi,yi,r):
    pygame.draw.circle(screen,(255,255,0),(xi,yi),r)
def line(xi,yi,xf,yf):
    pygame.draw.line(screen,(255,255,255),(xi,yi),(xf,yf),1)
def rect(xi,yi,w,h,blacktowhite):
    pygame.draw.rect(screen,(blacktowhite,blacktowhite,blacktowhite),(xi,yi,w,h))
def text(string,xi,yi):
    textsurface = font.render(string,False,(10,100,100))
    screen.blit(textsurface,(xi,yi))
def panel(xi,yi,string):
    w,h = 250,40
    pygame.draw.rect(screen,(25,25,255),(xi,yi,w,h))
    textsurface = font.render(string,False,(255,255,255))
    screen.blit(textsurface,(xi,yi))
def cursor(xi,yi):
    ri,re = 10,12
    pygame.draw.circle(screen,(0,0,0),(xi,yi),re)
    pygame.draw.circle(screen,(255,255,255),(xi,yi),ri)
def vaso(xi,yi,w,h,e):
    pygame.draw.rect(screen,(255,255,255),(xi,yi,w,h))
    pygame.draw.rect(screen,(0,0,0),(xi+e,yi,w-2*e,h-e))

X,Y,W,H = 100,100,500,300
lml = 40
wbs,hbs = 20,H-2*lml
sbmb = 1
sbmbsize = wbs-2*sbmb
downerlimit = Y+lml+sbmb
upperlimit = Y+lml+hbs-sbmb-sbmbsize
scrollbuttonrange = upperlimit- downerlimit
wsp,hsp = W-2*lml-2*wbs,H-2*lml
# elementos
n,m = 6,5
lme = 5
ew,eh = 70,70
element_list_top_limit = Y+lml+lme
element_list_range = (eh+10)*6
element_list_bottom_limit = element_list_top_limit-element_list_range+hsp

#### INICIALIZADORES ####
clicked = False
#### THE IMPORTANT STUFF OF DRAG AND DROP
class Key(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos,size,image,id):
        super(Key, self).__init__()
        self.image = pygame.image.load('images/'+image).convert()
        self.image = pygame.transform.scale(self.image,(size,size))
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.x = xpos 
        self.rect.y = ypos
        self.id = id
        self.linkready = False
        self.links = []
####
n,m = 6,5
#### TO IMPORT CODE INTO OTHER SCRPITS COPY THESE 3 LINES
button_image = pygame.image.load('button.png').convert()
button_image = pygame.transform.scale(button_image,(18,18))
##SBMB = Button(image=button_image, pos=(X+W-lml-wbs/2,Y+lml+sbmb+sbmbsize/2), 
##                    text_input="", font=get_font(35), base_color="#D2D2D2", hovering_color="Green")
#### THE IMPORTANT STUFF OF DRAG AND DROP
# THE SCROLL BUTTON
key_list = pygame.sprite.Group()# contenedor que guarda vrios sprites
key_list.add(Key(X+W-lml-wbs+sbmb,Y+lml+sbmb,18,'button.png',len(key_list)+1))# el primer y unico sprite
# THE CELLS
rows_list = [pygame.sprite.Group() for i in range(n)]
for row,element in enumerate(rows_list):
    for i in range(m):
        element.add(Key(X+lml+lme+i*(eh+lme),element_list_top_limit+row*(eh+10),70,'button.png',i+(row*5+1)))
# THE IMAGES/ICONS
icons_list = [pygame.sprite.Group() for i in range(n)]
for row,icon in enumerate(icons_list):
    for j in range(m):
        if j+(row*5+1) >= 25:
            break
        icon.add(Key(X+lml+lme+j*(eh+lme),element_list_top_limit+row*(eh+10),70,str(j+(row*5+1))+'.png',i+(row*5+1)))
    

####
####
while True:
    tiempo = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_q:
                pass
            if event.key == pygame.K_w:
                cur_vel_y = -10
            if event.key == pygame.K_a:
                cur_vel_x = -10
            if event.key == pygame.K_x:
                pass
            if event.key == pygame.K_d:
                cur_vel_x = 10
            if event.key == pygame.K_s:
                cur_vel_y = 10
            if event.key == pygame.K_n:
                pass
            if event.key == pygame.K_f:
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_q:
                pass
            if event.key == pygame.K_w:
                cur_vel_y = 0
            if event.key == pygame.K_e:
                pass
            if event.key == pygame.K_r:
                pass
            if event.key == pygame.K_a:
                cur_vel_x = 0
            if event.key == pygame.K_s:
                cur_vel_y = 0
            if event.key == pygame.K_d:
                cur_vel_x = 0
            if event.key == pygame.K_f:
                pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            if event.button == 1:
                for key in key_list:
                    if key.rect.collidepoint(pos):
                        key.clicked = True
                        for row in rows_list:
                            for element in row:
                                element.clicked = True
                        for row in icons_list:
                            for element in row:
                                element.clicked = True
                for i,row in enumerate(rows_list):
                    for j,element in enumerate(row):
                        if element.rect.collidepoint(pos):
                            print(element.id)
            elif event.button == 2:
                for key in key_list:
                    if key.rect.collidepoint(pos):
                        key.linkready = True
                        count = 0
                        links = []
                        for key in key_list :
                            if key.linkready == True:
                                count += 1
                                links.append(key.id)
                        if count == 2:
                            for key in key_list:
                                if key.linkready == True:
                                       key.linkready = False
                                       count += 1
                                       key.links += links

        if event.type == pygame.MOUSEBUTTONUP:
            for key in key_list:
                key.clicked = False
                for row in rows_list:
                    for element in row:
                        element.clicked = False
                for row in icons_list:
                    for element in row:
                        element.clicked = False
    screen.fill((0,0,0))
    # A partir de aqui dibujas
    #print(segundero)
    pos = pygame.mouse.get_pos()
    # SETTINGS
    # X,Y,W,H = 100,100,500,300
    #la ventana principal
    rect(X,Y,W,H,200)
    # la barra scroll
    lml = 40
    wbs,hbs = 20,H-2*lml
    rect(X+W-lml-wbs,Y+lml,wbs,hbs,150)
    #scroll mouse menu button
    sbmb = 1
    sbmbmsize = wbs-2*sbmb
    downerlimit = Y+lml+sbmb
    upperlimit = Y+lml+hbs-sbmb-sbmbsize
    scrollbuttonrange = upperlimit- downerlimit
##    rect(X+W-lml-wbs+sbmb,Y+lml+sbmb,sbmbmsize,sbmbmsize,210)
##    SBMB.update(screen)
    
    ####
    #showpanel
    wsp,hsp = W-2*lml-2*wbs,H-2*lml
    rect(X+lml,Y+lml,wsp,hsp,100)
    # elementos
    n,m = 6,5
    lme = 5
    ew,eh = 70,70
    element_list_top_limit = Y+lml+lme
    element_list_range = (eh+10)*6
    element_list_bottom_limit = element_list_top_limit-element_list_range+hsp
    for key in key_list:
        if key.clicked == True:
            if pos[1] < downerlimit:
                key.rect.y = downerlimit
            elif pos[1] > upperlimit:
                key.rect.y = upperlimit
            else:
                key.rect.y = pos[1]-(key.rect.height/2)
            
    key_list.draw(screen)
    

    for i,row in enumerate(rows_list):
        for j,element in enumerate(row):
            if element.clicked:
                if pos[1] < downerlimit:
                    element.rect.y = element_list_top_limit+i*(eh+10)
                elif pos[1] > upperlimit:
                    element.rect.y = element_list_bottom_limit+i*(eh+10)
                else:
                    element.rect.y = element_list_top_limit-(element_list_range-hsp)*((pos[1]-(element_list_top_limit))/scrollbuttonrange)+i*(eh+10)
            if element.rect.y > (Y+lml+lme-sbmbsize/3) and element.rect.y < (Y+lml+hsp-sbmbsize):
                row.draw(screen)
    for i,row in enumerate(icons_list):
        for j,element in enumerate(row):
            if element.clicked:
                if pos[1] < downerlimit:
                    element.rect.y = element_list_top_limit+i*(eh+10)
                elif pos[1] > upperlimit:
                    element.rect.y = element_list_bottom_limit+i*(eh+10)
                else:
                    element.rect.y = element_list_top_limit-(element_list_range-hsp)*((pos[1]-(element_list_top_limit))/scrollbuttonrange)+i*(eh+10)
            if element.rect.y > (Y+lml+lme-sbmbsize/3) and element.rect.y < (Y+lml+hsp-sbmbsize):
                row.draw(screen)

    #cursor
    cur_x += cur_vel_x
    cur_y += cur_vel_y

    #Aqui termina el loop
    segundero = segundero + 1
    pygame.display.update()
    clock.tick(30)
