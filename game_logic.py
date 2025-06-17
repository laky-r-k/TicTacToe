import pygame
import buttton_for_game
from Minimax import best_move
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
        if self.won!="tie":
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
    @staticmethod
    def check_tie(board):
        return 1 not in board
                


    @staticmethod
    def check_win(board):
        for i in range(0, 9, 3):
            if board[i] == board[i+1] == board[i+2] and board[i] != 1:
                if board[i] == "x":
                    return 1
                elif board[i] == "o":
                    return 2
    
        for i in range(0, 3):
            if board[i] == board[i+3] == board[i+6] and board[i] != 1:
                if board[i] == "x":
                    return 1
                elif board[i] == "o":
                    return 2
    
        if board[0] == board[4] == board[8] and board[0] != 1:
            if board[0] == "x":
                return 1
            elif board[0] == "o":
                return 2
    
        if board[2] == board[4] == board[6] and board[2] != 1:
            if board[2] == "x":
                return 1
            elif board[2] == "o":
                return 2
        return -1
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
                    self.check_win_tie()
                    if self.won is None:
                        self.playing=2
            elif self.playing==2:
                index=self.check_point_rect_lis(pos)
                if self.board[index]==1 and self.won==None:           
                    self.board[index]="o"
                    self.check_win_tie()
                    if self.won is None:
                        self.playing=1
        except:
            pass


    def play_with_bot(self, pos):
        if self.playing == 1 and self.won is None:
            index = self.check_point_rect_lis(pos)
            if index is not None and self.board[index] == 1:
                self.board[index] = "x"
                self.check_win_tie()
                if self.won is None:
                    self.playing=2
                    pygame.time.set_timer(pygame.USEREVENT, 500)
    
            
    def bot_move(self):            
        if self.playing == 2 and self.won is None:
            index = best_move(self.board,tac)  # best_move returns a valid index
            self.board[index] = "o"
            self.check_win_tie()
            if self.won is None:
                self.playing=1




    def check_win_tie(self):
        player=self.check_win(self.board)
        if self.check_tie(self.board) and player==-1:
            self.win_display("tie")
        elif player==1:
            self.win_display(1)
        elif player==2:
            self.win_display(2)

    
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

    