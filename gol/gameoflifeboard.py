from random import randrange

class gameoflifeboard(object):
    def __init__(self):
        self.boardInitiated = False
        self.x_size = 0
        self.boardsize_x = 0
        self.boardsize_y = 0
        self.board = []
                
    def createBoard(self, x_size, y_size):
        self.boardInitiated = True
        self.boardsize_x = x_size
        self.boardsize_y = y_size
        self.board = []
        for x in range(0,self.boardsize_x):  # @UnusedVariable
            self.board.append(["0"] * self.boardsize_y)
        
    def populate(self, ratio = 0.5):
        if ratio > 1 or ratio < 0:
            raise ValueError
        
        num_ones_set = 0        
        while num_ones_set < int(self.boardsize_x * self.boardsize_y * ratio):
            x = randrange(0, self.boardsize_x)
            y = randrange(0, self.boardsize_y)
            
            if self.board[x][y] != '1':
                self.board[x][y] = '1'
                num_ones_set += 1           