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
            elif event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                g.play_with_bot(pos)
                if  g.exit_button.is_button_pressed(pos):
                    g.run=False
                elif g.retry_button.is_button_pressed(pos):
                    g.reset()
            elif event.type == pygame.USEREVENT:
                g.bot_move()
                pygame.time.set_timer(pygame.USEREVENT, 0) 
            
        win.fill([250,250,250])
        g.draw_board()  
        g.check_display()
        g.chance_display()
        g.check_win_tie()
        
        
    
        pygame.display.update()
    pygame.quit()
main(win)