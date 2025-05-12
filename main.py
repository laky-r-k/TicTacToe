import pygame 
import game_logic

pygame.init()
width=1400
height=800
win=pygame.display.set_mode((width,height))

def main(win):
    g=game_logic.tac(win)
    g.upload_board()
    while g.run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                g.run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                g.play(pos)
                if  g.exit_button.is_button_pressed(pos):
                    g.run=False
                elif g.retry_button.is_button_pressed(pos):
                    g.reset()
            
        win.fill([250,250,250])
        g.draw_board()  
        g.check_display()
        g.chance_display()
        g.check_win()
        g.check_tie()
        
    
        pygame.display.update()
    pygame.quit()
main(win)