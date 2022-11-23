# button
class Button():# clase boton
    
        
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image # imagen que se carga desde el codigo principal

        #pos es una lista, array o tupla 
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        
        # aqui se pasa el "pygame.font.SysFont('Comic Sans MS', size)" del metodo get_font()
        # PLAY_TEXT = get_font(45).render("Bienvenido al simulador", True, "White")
        self.font = font # font=get_font(75)
        self.base_color, self.hovering_color = base_color, hovering_color # base_color="#d7fcd4", hovering_color="White"
        self.text_input = text_input # text_input="OPTIONS"
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None: # en caso de que no haya imagen de fondo
                self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

            


    def update(self, screen):
        if self.image is not None:
                screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
                self.text = self.font.render(self.text_input, True, self.base_color)
    def ifclicked(self):
        self.clicked = True

    def set_new_position(self,pos):
            # HEIGHT = 600
        self.rel_pos = pos
        print(self.rel_pos)
        self.y_pos = self.rel_pos
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
