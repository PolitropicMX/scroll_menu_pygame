import pygame, sys
from button import Button
import numpy as np
from math import *
from Mac_sprites import *
#### whats added
from class_projection import Draw3d
from draw import Draw
####

WIDTH, HEIGHT = 600,600
centro = [WIDTH/2,HEIGHT/2+100]
cubepos = centro
scale = 50

projection_matrix = np.matrix([
    [1,0,0],
    [0,1,0]])

pygame.display.set_caption("3D PROJECTION IN PYGAME")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

#### Whats added
DRAW3D = Draw3d(SCREEN,scale,centro)
DRAW = Draw()
TUBOS = Draw()
####

# letras
pygame.font.init()

#colores 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

pygame.init()


def rotation(anglex,angley,anglez):
    rotation_z = np.matrix([
        [cos(anglez),-sin(anglez),0],
        [sin(anglez),cos(anglez),0],
        [0,0,1]
        ])

    rotation_y = np.matrix([
        [cos(angley),0,sin(angley)],
        [0,1,0],
        [-sin(angley),0,cos(angley),]
        ])

    rotation_x = np.matrix([
        [1,0,0],
        [0,cos(anglex),-sin(anglex)],
        [0,sin(anglex),cos(anglex)]
        ])
    return rotation_x, rotation_y, rotation_z

def textvector(string,titlespos,scale,cubepos,rotation_x, rotation_y, rotation_z):
    for title in titlespos:
        title2d = np.dot(rotation_z, title.reshape((3,1)))
        title2d = np.dot(rotation_y, title2d)
        title2d = np.dot(rotation_x, title2d)
        title = np.dot(projection_matrix, title2d)
        x = int(title[0][0] * scale) + cubepos[0]
        y = int(title[1][0] * scale) + cubepos[1]
        DRAW3D.text(string,x,y,32,'Black')


obj_list = []# Stores all the positions where an object is
who_list = []# Stores who occupies the position that is located at the same index
#in the obj_list, so there's 2 list with the same length that
# stores a matrix position and a string with reference to what sprite
# correponds
# bomba 1
obj_list.append(np.matrix([2.5,-0.5,-1.5]))
who_list.append('8')
# bomba 2
obj_list.append(np.matrix([2.5,-0.5,2.5]))
who_list.append('8')
# bomba 3
obj_list.append(np.matrix([-1.5,-0.5,1.5]))
who_list.append('8')
#tanque1
obj_list.append(np.matrix([0.5,-0.5,0.5]))
who_list.append('1')
# tanque2
obj_list.append(np.matrix([0.5,-0.5,-1.5]))
who_list.append('1')
# tanque3
obj_list.append(np.matrix([0.5,-0.5,2.5]))
who_list.append('1')
# enfriador
obj_list.append(np.matrix([1.5,-2,1.5]))
who_list.append('10')
# calandria 1
obj_list.append(np.matrix([2.5,-5,2.5]))
who_list.append('2')
# calandria 2
obj_list.append(np.matrix([2.5,-4,2.5]))
who_list.append('3')
# condensador 1
obj_list.append(np.matrix([-1.5,-4.5,0.5]))
who_list.append('6')
# condensador 2
obj_list.append(np.matrix([-1.5,-3.5,0.5]))
who_list.append('7')
# condensador 3
obj_list.append(np.matrix([-1.5,-4.5,-0.5]))
who_list.append('6')
# condensador 4
obj_list.append(np.matrix([-1.5,-3.5,-0.5]))
who_list.append('7')
# SEPARADOR
obj_list.append(np.matrix([2.5,-6.5,0.5]))
who_list.append('9')




tubop1 = DRAW3D.tubo((-0.5,-1.5,-5),(-0.5,-1.5,5))
tubord1 = DRAW3D.tubo(([-0.5,-1.5,0.5]),(0.5,-1.5,0.5))
tubord2 = DRAW3D.tubo((0.5,-1.5,-1.5),(0.5,-1.5,-1.5))
tubord22 = DRAW3D.tubo((0.5,-0.15,-1.5),(2.5,-0.15,-1.5))
tubord222 = DRAW3D.tubo((2.5,-0.15,-1.5),(2.5,-3.5,-1.5))
tubord2222 = DRAW3D.tubo((2.5,-3.5,-1.5),(2.5,-3.5,0.5))

bomba = DRAW3D.cubo((2.5,-0.15,-1.5),0.5)
bomba2 = DRAW3D.cubo((2.5,-0.15,0.5),0.5)

rotametro = DRAW3D.cubo((2.5,-2.5,-1.5),0.5)

tablero = DRAW3D.cubo((2.5,-2.5,-0.5),1)

calandria1 = DRAW3D.cubo((2.5,-4.5,2.5),1)
calandria2 = DRAW3D.cubo((2.5,-3.5,2.5),1)

sep_ciclonico = DRAW3D.cubo((2.5,-6.5,0.5),1)

condensador1 = DRAW3D.cubo((-1.5,-4.5,0.5),1)
condensador11 = DRAW3D.cubo((-1.5,-3.5,0.5),1)
condensador111 = DRAW3D.cubo((-1.5,-4.5,-0.5),1)
condensador1111 = DRAW3D.cubo((-1.5,-3.5,-0.5),1)

##DRAW3D.tubord3 = DRAW3D.tubo((-0.5,-1.5,2.5),(0.5,-1.5,2.5))
tuborc1 = DRAW3D.tubo((2.5,-6,0.5),(2.5,-0.15,0.5))
tuborc2 = DRAW3D.tubo((2.5,-0.15,0.5),(2.5,-0.15,2.5))
tuborc3 = DRAW3D.tubo((2.5,-0.15,2.5),(2.5,-3.5,2.5))
tuborc4 = DRAW3D.tubo((2.5,-5.5,2.5),(2.5,-6.5,2.5))
tuborc5 = DRAW3D.tubo((2.5,-6.5,2.5),(2.5,-6.5,1))
tubodes1 = DRAW3D.tubo((2.5,-6.5,0),(2.5,-6.5,-0.5))
tubodes11 = DRAW3D.tubo((2.5,-6.5,-0.5),(-1.5,-6.5,-0.5))
tubodes111 = DRAW3D.tubo((-1.5,-6.5,-0.5),(-1.5,-5,-0.5))
tubodes1111 = DRAW3D.tubo((-1.5,-5,0.5),(-1.5,-5.5,0.5))
tubodes11111 = DRAW3D.tubo((-1.5,-5.5,0.5),(-1.5,-5.5,1.5))
tubodes111111 = DRAW3D.tubo((-1.5,-5.5,1.5),(-1.5,-0.5,1.5))
tubowst1 = DRAW3D.tubo((-0.5,0.5,-5),(-0.5,0.5,5))
tubovap1 = DRAW3D.tubo((0.5,-5,-5),(0.5,-5,5))
tubovap11 = DRAW3D.tubo((0.5,-5,2.5),(2,-5,2.5))
tubovap111 = DRAW3D.tubo((1,-5,2.5),(1,-3,2.5))
tubovap1111 = DRAW3D.tubo((1,-3,2.5),(0.5,-3,2.5))
tubovap11111 = DRAW3D.tubo((0.5,-3,2.5),(0.5,-1,2.5))
tubovap12 = DRAW3D.tubo((2.5,-4,2),(2.5,-4,1.5))
tubovap122 = DRAW3D.tubo((2.5,-4,1.5),(2.5,-2,1.5))
tubovap1222 = DRAW3D.tubo((2.5,-2,1.5),(2.5,-2,1.5))
tubovap12222 = DRAW3D.tubo((2.5,-2,1.5),(2,-2,1.5))
tuboenf = DRAW3D.tubo((1,-2,1.5),(0.5,-2,1.5))
tuboenf1 = DRAW3D.tubo((0.5,-2,1.5),(0.5,-2,0.5))
tuboenf11 = DRAW3D.tubo((0.5,-2,0.5),(0.5,-1,0.5))
##DRAW3D.tuboenf111 = tubo((1,-2,1.5),(0.5,-2,1.5))

j = 5
titlesposx = [np.matrix([j,0,0])]
titlesposy = [np.matrix([[0,j,0]])]
titlesposz = [np.matrix([[0,0,j]])]

guidelines = []
guidelines.append(np.matrix([2,0,0]))
guidelines.append(np.matrix([-2,0,0]))
guidelines.append(np.matrix([0,2,0]))
guidelines.append(np.matrix([0,-2,0]))
guidelines.append(np.matrix([0,0,2]))
guidelines.append(np.matrix([0,0,-2]))

centrocubo = [0,0,0]
points = DRAW3D.cubo(centrocubo,1)
tanque1 = DRAW3D.cubo((0.5,-0.5,0.5),1)
tanquetitle1 = [np.matrix([0.5,-0.5,0.5])]
tanque2 = DRAW3D.cubo((0.5,-0.5,-1.5),1)
tanquetitle2 = [np.matrix([0.5,-0.5,-1.5])]
tanque3 = DRAW3D.cubo((0.5,-0.5,2.5),1)
tanquetitle3= [np.matrix([0.5,-0.5,2.5])]

n = 5
plane = DRAW3D.planemaker(n)


## AQUI VIENE LO CHIDO: Mac_sprites

# variables controladas por el teclado e incrementos
anglex = 0
angley = 0
anglez = 0
velanglex = 0
velangley = 0
velanglez = 0
option1 = 1
option2 = 0



def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont("f", size)

def play():
    anglex = 0
    angley = 0
    anglez = 0
    velanglex = 0
    velangley = 0
    velanglez = 0
    option1 = 1
    option2 = 0
    segundero = 0
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("White")

        PLAY_TEXT = get_font(35).render("PLAY SCREEN.", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(200, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(70, HEIGHT-45), 
                            text_input="BACK", font=get_font(35), base_color="Black", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_q:
                    velanglez = -0.1
                    dimension = 3
                if event.key == pygame.K_w:
                    velanglex = -0.1
                    dimension = 1
                if event.key == pygame.K_a:
                    velangley = 0.1
                    dimension = 2
                if event.key == pygame.K_e:
                    velanglez = 0.1
                    dimension = 3
                if event.key == pygame.K_d:
                    velangley = -0.1
                    dimension = 2
                if event.key == pygame.K_s:
                    velanglex = 0.1
                    dimension = 1
                if event.key == pygame.K_1:
                    option1 = 1
                if event.key == pygame.K_2:
                    option2 = 1
                if event.key == pygame.K_f:
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_q:
                    velanglez = 0
                if event.key == pygame.K_w:
                    velanglex = 0
                if event.key == pygame.K_e:
                    velanglez = 0
                if event.key == pygame.K_r:
                    pass
                if event.key == pygame.K_a:
                    velangley = 0
                if event.key == pygame.K_s:
                    velanglex = 0
                if event.key == pygame.K_d:
                    velangley = 0
                if event.key == pygame.K_f:
                    pass
                if event.key == pygame.K_1:
                    option1 = 0
                if event.key == pygame.K_2:
                    option2 = 0
                        
        anglez  += velanglez
        angley  += velangley
        anglex  += velanglex
        
        # ROTACIONES
        rotation_x, rotation_y, rotation_z = rotation(anglex,angley,anglez)
        #### whats added
        DRAW3D.set_rotations([rotation_x, rotation_y, rotation_z])
        # ETIQUETA DE LOS EJES
        textvector('Y',titlesposy,scale,centro,rotation_x,rotation_y,rotation_z)
        textvector('X',titlesposx,scale,centro,rotation_x,rotation_y,rotation_z)
        textvector('Z',titlesposz,scale,centro,rotation_x,rotation_y,rotation_z)
        DRAW3D.projection(guidelines,True,'star',red)
        # IMAGENES
        

        # EL PLANO
        DRAW3D.flatsurface(n,plane)

        # DRAWTUBE
        DRAW3D.drawtubo(tubord22,True,segundero,'liq',True)
##        DRAW3D.drawtubo(tubord3,True,segundero,'liq',True)

        images = addimages(obj_list,who_list,scale,centro,rotation_x, rotation_y, rotation_z)# this is a SPrite group and has a method called draw
        images.draw(SCREEN)
        DRAW3D.drawtubo(tubowst1,True,segundero,'wst',True)
        DRAW3D.drawtubo(tubop1,True,segundero,'liq',True)
        DRAW3D.drawtubo(tubord2,True,segundero,'liq',True)

        DRAW3D.drawtubo(tubord222,True,segundero,'liq',True)
        DRAW3D.drawtubo(tubord2222,True,segundero,'liq',True)
        DRAW3D.drawtubo(tuborc1,True,segundero,'liq',True)
        DRAW3D.drawtubo(tuborc2,True,segundero,'liq',True)
        DRAW3D.drawtubo(tuborc3,True,segundero,'liq',True)
        DRAW3D.drawtubo(tuborc4,True,segundero,'liq',True)
        DRAW3D.drawtubo(tuborc5,True,segundero,'liq',True)
        DRAW3D.drawtubo(tubodes1,True,segundero,'liq',True)
        DRAW3D.drawtubo(tubodes11,True,segundero,'liq',True)
        DRAW3D.drawtubo(tubodes111,True,segundero,'liq',True)
        DRAW3D.drawtubo(tubodes1111,True,segundero,'liq',True)
        DRAW3D.drawtubo(tubodes11111,True,segundero,'liq',True)
        DRAW3D.drawtubo(tubodes111111,True,segundero,'liq',True)
        DRAW3D.drawtubo(tubovap1,True,segundero,'vap',True)
        DRAW3D.drawtubo(tubovap11,True,segundero,'vap',True)
        DRAW3D.drawtubo(tubovap111,True,segundero,'vap',True)
        DRAW3D.drawtubo(tubovap1111,True,segundero,'vap',True)
        DRAW3D.drawtubo(tubovap11111,True,segundero,'vap',True)
        DRAW3D.drawtubo(tubovap12,True,segundero,'vap',True)
        DRAW3D.drawtubo(tubovap122,True,segundero,'vap',True)
        DRAW3D.drawtubo(tubovap1222,True,segundero,'vap',True)
        DRAW3D.drawtubo(tubovap12222,True,segundero,'vap',True)
        DRAW3D.drawtubo(tuboenf,True,segundero,'liq',True)
        DRAW3D.drawtubo(tuboenf1,True,segundero,'liq',True)
        DRAW3D.drawtubo(tuboenf11,True,segundero,'liq',True)
        segundero += 1
        pygame.display.update()

def create():
    anglex = 0
    angley = 0
    anglez = 0
    velanglex = 0
    velangley = 0
    velanglez = 0
    option1 = 1
    option2 = 0
    segundero = 0
    #### XXX COPY THIS TO IMPORT THE MURDERER TO OTHERS CODE
    the_murder_coordinate = [np.matrix([0,0,0])]
    player_x = 0.5
    player_y = 0.5
    player_z = 0.5
    player_x_vel = 0
    player_y_vel = 0
    player_z_vel = 0
    ismenuRunning = False
    cwho = []
    menuimg = pygame.sprite.Group()
    ####
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CLEAR_BUTTON.checkForInput(mouse):
                    DRAW.clear()
                    TUBOS.clear()
                    memory = {}
                    cwho = []
                if UNDO_BUTTON.checkForInput(mouse):
                    DRAW.undo()
                    cwho = cwho[0:(len(cwho)-1)]
                if BACK_BUTTON.checkForInput(mouse):
                    main_menu()
            if event.type == pygame.KEYDOWN:
                ## XXX COPY THIS TO IMPORT THE MURDERER TO OTHERS CODE
                # THE ENVIRONTMENT
                if event.key == pygame.K_q:# Z dir
                    velanglez = -0.05
                if event.key == pygame.K_w:# x dir
                    velanglex = -0.05
                if event.key == pygame.K_a:# y dir
                    velangley = 0.05
                if event.key == pygame.K_e:# z dir
                    velanglez = 0.05
                if event.key == pygame.K_d:# y dir
                    velangley = -0.05
                if event.key == pygame.K_s:# x dir
                    velanglex = 0.05
                ## XXX COPY THIS TO IMPORT THE MURDERER TO OTHERS CODE
                # THE MURDER CONTROL PLACE
                if event.key == pygame.K_u:# y dir
                    player_y_vel = 0.05
                if event.key == pygame.K_i:# x dir
                    player_x_vel = 0.05
                if event.key == pygame.K_o:# Z dir
                    player_y_vel = -0.05
                if event.key == pygame.K_l:# x dir
                    player_z_vel = 0.05
                if event.key == pygame.K_k:# Z dir
                    player_x_vel = -0.05
                if event.key == pygame.K_j:# Z dir
                    player_z_vel = -0.05
                if event.key == pygame.K_0:
                    if ismenuRunning:
                        cwho.append('10')
                    ismenuRunning = False
                if event.key == pygame.K_1:
                    if ismenuRunning:
                        cwho.append('1')
                    ismenuRunning = False
                if event.key == pygame.K_2:
                    if ismenuRunning:
                        cwho.append('2')
                    ismenuRunning = False
                if event.key == pygame.K_3:
                    if ismenuRunning:
                        cwho.append('3')
                    ismenuRunning = False
                if event.key == pygame.K_4:
                    if ismenuRunning:
                        cwho.append('4')
                    ismenuRunning = False
                if event.key == pygame.K_5:
                    if ismenuRunning:
                        cwho.append('5')
                    ismenuRunning = False
                if event.key == pygame.K_6:
                    if ismenuRunning:
                        cwho.append('6')
                    ismenuRunning = False
                if event.key == pygame.K_7:
                    if ismenuRunning:
                        cwho.append('7')
                    ismenuRunning = False
                if event.key == pygame.K_8:
                    if ismenuRunning:
                        cwho.append('8')
                    ismenuRunning = False
                if event.key == pygame.K_9:
                    if ismenuRunning:
                        cwho.append('9')
                    ismenuRunning = False
                if event.key == pygame.K_2:
                    option2 = 1
##            XXX WHEN ADDING A 3D POINT
                if event.key == pygame.K_f:
                    if not ismenuRunning:
                        DRAW.add3dpoint([halo_x,halo_y,halo_z],False)
                    ismenuRunning = True
    ##            XXX
                if event.key == pygame.K_t:
                    TUBOS.add3dpoint([halo_x,halo_y,halo_z],False)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_UP:
                    pass
                ## XXX COPY THIS TO IMPORT THE MURDERER TO OTHERS CODE
                # THE ENVIRONTMENT UP Keys
                if event.key == pygame.K_q:
                    velanglez = 0
                if event.key == pygame.K_w:
                    velanglex = 0
                if event.key == pygame.K_e:
                    velanglez = 0
                if event.key == pygame.K_a:
                    velangley = 0
                if event.key == pygame.K_s:
                    velanglex = 0
                if event.key == pygame.K_d:
                    velangley = 0
                if event.key == pygame.K_1:
                    option1 = 0
                if event.key == pygame.K_2:
                    option2 = 0
                # WHEN KEY MURDERER ARE ALL UP
                if event.key == pygame.K_u:# y dir
                    player_y_vel = 0
                if event.key == pygame.K_i:# x dir
                    player_x_vel = 0
                if event.key == pygame.K_o:# Z dir
                    player_y_vel = -0
                if event.key == pygame.K_l:# x dir
                    player_z_vel = 0
                if event.key == pygame.K_k:# Z dir
                    player_x_vel = -0
                if event.key == pygame.K_j:# Z dir
                    player_z_vel = -0

        
        #print(dimension)
        SCREEN.fill("White")
        #estrutura de sprites en el espacio 3d
        memory, lines = DRAW.get_3d_info()
        #estructura para el dibujado de lineas
        tubos_memoria,extremos_tubos = TUBOS.get_3d_info()
        proj = DRAW3D.projection(tubos_memoria,False,'no','no')
        TUBOS.set_2d_proj(proj)
        TUBOS.line3d(SCREEN,(20,50,70),False)
        rotation_x, rotation_y, rotation_z = rotation(anglex,angley,anglez)
        DRAW3D.set_rotations([rotation_x, rotation_y, rotation_z])
        DRAW3D.projection(titlesposy,False,'Y',"Black")
        DRAW3D.projection(titlesposx,False,'X',"Black")
        DRAW3D.projection(titlesposz,False,'Z',"Black")
        DRAW3D.projection(guidelines,True,'star',"Green")
        DRAW3D.flatsurface(n,plane)
        ## XXX COPY THIS TO IMPORT THE MURDERER TO ANOTHER CODE
        # adding to the position 
        player_x += player_x_vel
        player_y += player_y_vel
        player_z += player_z_vel
        # ESTABLECEMOS LAS COORDENADAS INICIALES EN Murderer
        the_murder_coordinate = [np.matrix([player_x,player_y,player_z])]# incrementos en 3d
        DRAW3D.draw_the_murder(the_murder_coordinate)
        # XXXX THE MURDERER CUBE XXXX
        halo_x = ceil(player_x)-0.5
        halo_y = ceil(player_y)-0.5
        halo_z = ceil(player_z)-0.5
        DRAW3D.drawcube(DRAW3D.cubo((halo_x,halo_y,halo_z),1),False)
        DRAW3D.text(str([halo_x,halo_y,halo_z]),200,20,20,"Blue")   
        anglez += velanglez
        angley += velangley
        anglex += velanglex
        segundero += 1
        # 3 lineas obigatorias para escribir un boton
        CLEAR_BUTTON = Button(image=None, pos=(80, 550), 
                            text_input="CLEAR", font=get_font(25), base_color="Black", hovering_color="Blue")
        CLEAR_BUTTON.changeColor(mouse)
        CLEAR_BUTTON.update(SCREEN)
        # 3 lineas obigatorias para escribir un boton
        UNDO_BUTTON = Button(image=None, pos=(140, 550), 
                            text_input="UNDO", font=get_font(25), base_color="Black", hovering_color="Blue")
        UNDO_BUTTON.changeColor(mouse)
        UNDO_BUTTON.update(SCREEN)
        # 3 lineas obigatorias para escribir un boton
        BACK_BUTTON = Button(image=None, pos=(400, 550), 
                            text_input="BACK", font=get_font(25), base_color="Black", hovering_color="Blue")
        BACK_BUTTON.changeColor(mouse)
        BACK_BUTTON.update(SCREEN)
        if ismenuRunning:
            x,y,w,h = 50,70,500,200
            g,p = 10,10
            e = (w-2*p)/5
            f = (h-2*g)/2
            nb = (w)/5
            mn = (h)/2
            pygame.draw.rect(SCREEN,(0,0,0),(x,y,w,h))
            count = 1

            menuimg = images = pygame.sprite.Group()
            for i in range(2):
                for j in range(5):
                    pygame.draw.rect(SCREEN,(50,50,50),(x+p+j*e,y+g+i*f,e-p,e-p))
                    menuimg.add(Mac(x+50+j*nb,y+50+i*mn,str(count),scale,i))
                    count+= 1
            menuimg.draw(SCREEN)
        # Se necesita tener una lista de posiciones 3d y de identificadores
        # del mismo tamamo
        if len(cwho) > 0 and len(memory) == len(cwho):
            images = addimages(memory,cwho,scale,centro,rotation_x, rotation_y, rotation_z)
            images.draw(SCREEN)
        #print(segundero)
        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("White")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS SCREEN.", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(70, HEIGHT-45))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(70, HEIGHT-45), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    anglex = 0
    angley = 0
    anglez = 0
    velanglex = 0
    velangley = 0
    velanglez = 0
    option1 = 1
    option2 = 0
    segundero = 0
    while True:
        SCREEN.fill("White")
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(30).render("MAIN MENU", True, "#b68f40")
        cx = 100
        MENU_RECT = MENU_TEXT.get_rect(center=(cx, 20))

        PLAY_BUTTON = Button(image=None, pos=(cx, 50), 
                            text_input="PLAY", font=get_font(35), base_color=(100,200,0), hovering_color="Black")
        OPTIONS_BUTTON = Button(image=None, pos=(cx, 80), 
                            text_input="OPTIONS", font=get_font(25), base_color=(100,200,0), hovering_color="Black")
        CREATE_BUTTON = Button(image=None, pos=(cx, 100), 
                            text_input="CREATE_ANIMATION", font=get_font(25), base_color=(100,200,0), hovering_color="Black")
        QUIT_BUTTON = Button(image=None, pos=(cx, 120), 
                            text_input="QUIT", font=get_font(25), base_color=(100,200,0), hovering_color="Black")
        
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, CREATE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if CREATE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    create()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_q:
                    velanglez = -0.1
                    dimension = 3
                if event.key == pygame.K_w:
                    velanglex = -0.1
                    dimension = 1
                if event.key == pygame.K_a:
                    velangley = 0.1
                    dimension = 2
                if event.key == pygame.K_e:
                    velanglez = 0.1
                    dimension = 3
                if event.key == pygame.K_d:
                    velangley = -0.1
                    dimension = 2
                if event.key == pygame.K_s:
                    velanglex = 0.1
                    dimension = 1
                if event.key == pygame.K_1:
                    option1 = 1
                if event.key == pygame.K_2:
                    option2 = 1
                if event.key == pygame.K_f:
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_q:
                    velanglez = 0
                if event.key == pygame.K_w:
                    velanglex = 0
                if event.key == pygame.K_e:
                    velanglez = 0
                if event.key == pygame.K_r:
                    pass
                if event.key == pygame.K_a:
                    velangley = 0
                if event.key == pygame.K_s:
                    velanglex = 0
                if event.key == pygame.K_d:
                    velangley = 0
                if event.key == pygame.K_f:
                    pass
                if event.key == pygame.K_1:
                    option1 = 0
                if event.key == pygame.K_2:
                    option2 = 0
                        
        anglez  = 0
        angley  = -0.6
        anglex  = -0.6

        
        # ROTACIONES
        rotation_x, rotation_y, rotation_z = rotation(anglex,angley,anglez)
        DRAW3D.set_rotations([rotation_x, rotation_y, rotation_z])
        # IMAGENES
        images = addimages(obj_list,who_list,scale,centro,rotation_x, rotation_y, rotation_z)
        images.draw(SCREEN)
        # ETIQUETA DE LOS EJES
        textvector('Y',titlesposy,scale,centro,rotation_x,rotation_y,rotation_z)
        textvector('X',titlesposx,scale,centro,rotation_x,rotation_y,rotation_z)
        textvector('Z',titlesposz,scale,centro,rotation_x,rotation_y,rotation_z)
        DRAW3D.projection(guidelines,True,'star',red)

        # EL PLANO
        DRAW3D.flatsurface(n,plane)

        # DRAWCUBE
        DRAW3D.drawcube(tanque1,False)
        textvector('1',tanquetitle1,scale,centro,rotation_x,rotation_y,rotation_z)

        DRAW3D.drawcube(tanque2,False)
        textvector('2',tanquetitle2,scale,centro,rotation_x,rotation_y,rotation_z)

        DRAW3D.drawcube(tanque3,False)
        textvector('3',tanquetitle3,scale,centro,rotation_x,rotation_y,rotation_z)

        DRAW3D.drawcube(bomba,False)
        DRAW3D.drawcube(rotametro,False)

        DRAW3D.drawcube(tablero,False)
        DRAW3D.drawcube(calandria1,False)
        DRAW3D.drawcube(calandria2,False)
        DRAW3D.drawcube(sep_ciclonico,False)

        DRAW3D.drawcube(condensador1,False)
        DRAW3D.drawcube(condensador11,False)
        DRAW3D.drawcube(condensador111,False)
        DRAW3D.drawcube(condensador1111,False)

        # DRAWTUBE
        DRAW3D.drawtubo(tubop1,True,segundero,'liq',True)
        DRAW3D.drawtubo(tubord1,True,segundero,'liq',True)
        DRAW3D.drawtubo(tubord2,True,segundero,'liq',True)
        DRAW3D.drawtubo(tubord22,True,segundero,'liq',True)

        DRAW3D.drawtubo(tubord222,True,segundero,'liq',True)
        DRAW3D.drawtubo(tubord2222,True,segundero,'liq',True)
        DRAW3D.drawtubo(tuborc1,True,segundero,'liq',True)
        DRAW3D.drawtubo(tuborc2,True,segundero,'liq',True)
        DRAW3D.drawtubo(tuborc3,True,segundero,'liq',True)
        DRAW3D.drawtubo(tuborc4,True,segundero,'liq',True)
        DRAW3D.drawtubo(tuborc5,True,segundero,'liq',True)
        DRAW3D.drawtubo(tubodes1,True,segundero,'liq',True)
        DRAW3D.drawtubo(tubodes11,True,segundero,'liq',True)
        DRAW3D.drawtubo(tubowst1,True,segundero,'wst',True)
        DRAW3D.drawtubo(tubovap1,True,segundero,'vap',True)
        DRAW3D.drawtubo(tubovap11,True,segundero,'vap',True)
        
        segundero += 1
        pygame.display.update()

main_menu()

