import pygame
import buttton_for_game
class tac:
    def __init__(self,win):
        self.board=[1,1,1,1,1,1,1,1,1]
        self.rect_ls=[]
        self.x_image=pygame.transform.scale(pygame.image.load("x_image.png"),(190,190))
        self.y_image=pygame.transform.scale(pygame.image.load("o_image.png"),(190,190))
        self.win=win
        self.playing=1
        self.run=True
        self.won=None
        color=[0,0,0]
        bg_color=[20,250,250]
        self.exit_button=buttton_for_game.button("exit",color,bg_color,20,50,[680,460])
        self.retry_button=buttton_for_game.button("retry",color,bg_color,20,50,[770,460])
    def upload_board(self):
        for i in range(400,1000,200):
            for j in range(100,600,200):
                self.rect_ls.append(pygame.Rect(i,j,200,200))
    def check_display(self):
        for i in range(9):
            if self.board[i]=="x":
                self.win.blit(self.x_image,(self.rect_ls[i].x+5,self.rect_ls[i].y+5))
            elif self.board[i]=="o":
                self.win.blit(self.y_image,(self.rect_ls[i].x+5,self.rect_ls[i].y+5))
    def win_display(self,player):
        self.won=player
        font_o=pygame.font.SysFont("BOLD",50)
        if self.won!=None:
            surface=pygame.font.Font.render(font_o,"player "+str(player)+" won ",True,[0,0,0])
        else:
            surface=pygame.font.Font.render(font_o," tie",True,[0,0,0])  
        X=1500/2-250
        Y=800/2-100
        pygame.draw.rect(self.win,[250,250,200],pygame.Rect(X,Y,500,200))
        self.win.blit(surface,(X+110,Y+70)) 
        self.exit_button.create_button(self.win)
        self.retry_button.create_button(self.win)
    def chance_display(self):
        font_o=pygame.font.SysFont("BOLD",50)
        surface=pygame.font.Font.render(font_o,"chance: player"+str(self.playing),True,[0,0,0])  
        self.win.blit(surface,(0,0)) 
    def check_tie(self):
        if self.won==None:
            found_1=False
            for i in self.board:
                if i==1:
                    found_1=True
            if not found_1 :
                self.win_display(None)


    
    def check_win(self):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] and self.board[i] != 1:
                if self.board[i] == "x":
                    self.win_display(1)
                elif self.board[i] == "o":
                    self.win_display(2)
    
        for i in range(0, 3):
            if self.board[i] == self.board[i+3] == self.board[i+6] and self.board[i] != 1:
                if self.board[i] == "x":
                    self.win_display(1)
                elif self.board[i] == "o":
                    self.win_display(2)
    
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != 1:
            if self.board[0] == "x":
                self.win_display(1)
            elif self.board[0] == "o":
                self.win_display(2)
    
        if self.board[2] == self.board[4] == self.board[6] and self.board[2] != 1:
            if self.board[2] == "x":
                self.win_display(1)
            elif self.board[2] == "o":
                self.win_display(2)
    def check_point_rect_lis(self,pos):
        for rec in range(len(self.rect_ls)) :
            if pygame.Rect.collidepoint(self.rect_ls[rec],pos[0],pos[1]):
                return rec
    def play(self,pos):
        try:
            if self.playing==1:
                index=self.check_point_rect_lis(pos)
                if self.board[index]==1 and self.won==None:
                    self.board[index]="x"
                    self.playing=2
            elif self.playing==2:
                index=self.check_point_rect_lis(pos)
                if self.board[index]==1 and self.won==None:           
                    self.board[index]="o"
                    self.playing=1
        except:
            pass

    
    def draw_board(self):
        pygame.draw.line(self.win,[0,0,0],[600,100],[600,700])
        pygame.draw.line(self.win,[0,0,0],[800,100],[800,700])
        pygame.draw.line(self.win,[0,0,0],[400,300],[1000,300])
        pygame.draw.line(self.win,[0,0,0],[400,500],[1000,500])
    def reset(self):
        self.board=[1,1,1,1,1,1,1,1,1]
        self.playing=1
        self.won=None
        self.retry_button.is_created=False
        self.exit_button.is_created=False

    