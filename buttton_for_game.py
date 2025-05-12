import pygame
pygame.init()
class button:
    pressed=False
    def __init__(self,name,textcolor,back_color,height,width,cordinates):
        self.name=name
        self.textcolor=textcolor
        self.back_color=back_color
        self.height=height
        self.width=width
        self.font=pygame.font.SysFont(self.name,self.height)
        self.rect=pygame.Rect(cordinates[0],cordinates[1],width + 10,height+10)
        surface_text=pygame.font.Font.render(self.font,self.name,True,self.textcolor)
        self.surface_text=pygame.transform.scale(surface_text,[self.width,self.height])
        self.is_created=False

    def create_button(self,surface): 
        pygame.draw.rect(surface,self.back_color,self.rect)
        surface.blit(self.surface_text,[self.rect[0]+5,self.rect[1]+5])
        self.is_created=True
    
    def is_button_pressed(self,position):                                              #change made in 2/01/2024 is_button_pressed returns true only when create_button is already exectuted by using self.is_created 
        check=False
        if self.is_created:
            check=pygame.Rect.collidepoint(self.rect,position[0],position[1])
        return check
    def create_elips_button(self,surface):
        pygame.draw.ellipse(surface,self.back_color,pygame.Rect(self.rect.x-3,self.rect.y-2,self.rect.width+5,self.rect.height+5))
        surface.blit(self.surface_text,[self.rect[0]+5,self.rect[1]+5])
        self.is_created=True
    
    

    