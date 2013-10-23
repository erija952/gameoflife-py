from gol.outputformater import outputformater
import gameoflifeboard
import platform
import subprocess
import numpy as np

class gameoflife(object):

    def __init__(self):        
        pass
    
    def run(self):
        golb = gameoflifeboard.gameoflifeboard()
        golb.createBoard(10, 10)
        golb.populate()
        board = golb.board
        print board
        myinput = ''
        while myinput != 'c':
            board = self.update_board(board)
            of = outputformater(u'\u25FC',u'\u25FD')
            of.output(board)
            myinput = raw_input(':')
            self.clear()         
        
    def clear(self):
        subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell=True)
        
    def count_neighbours(self, y, x, board):       
        (max_rows,max_cols) = np.shape(board)
        #todo: assumes board large than 2*2
        nr_neighbours = 0       
        for yi in range(-1,2):           
            for xi in range(-1,2):
                curx=x+xi
                cury=y+yi
                if not(xi == 0 and yi == 0): #Don't count current coordinate
                    if curx >= 0 and curx < max_rows:
                        if cury >= 0 and cury < max_cols:
                            if board[cury][curx] == '1':
                                nr_neighbours +=1
        return nr_neighbours 
    
    def live_cell_survives_to_next_generation_r1r2r3(self, nr_neighbours):
        if nr_neighbours == 2 or nr_neighbours == 3:
            return True
        else:
            return False
        
    def dead_cell_resurrects_r4(self, nr_neighbours):
        if nr_neighbours == 3:
            return True
        else:
            return False
    
    def update_board(self,board):
        (rows,cols) = np.shape(board)
        new_board = []
        for x in range(0,rows):  # @UnusedVariable
            new_board.append(["0"] * cols)        
                    
        for y in range(0,cols):
            for x in range(0,rows):
                nr_neighbours = self.count_neighbours(y, x, board)
                               
                if board[y][x] == '1':
                    if self.live_cell_survives_to_next_generation_r1r2r3(nr_neighbours):
                        new_board[y][x] = '1'
                else:
                    if self.dead_cell_resurrects_r4(nr_neighbours):
                        new_board[y][x] = '1'
        return new_board
