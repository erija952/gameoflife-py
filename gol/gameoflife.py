from gol.outputformater import outputformater
import gameoflifeboard
import platform
import subprocess
import numpy as np

class gameoflife(object):

    def __init__(self):        
        pass
    
    def run(self):
        myinput = ''
        while myinput != 'c':
            self.update()
            myinput = raw_input(':')
            self.clear()         
    
    def update(self):
        golBoard = gameoflifeboard.gameoflifeboard()
        golBoard.createBoard(5,5)
        golBoard.populate()
        of = outputformater(u'\u25FC',u'\u25FD')
        of.output(golBoard.board)               
        
    def clear(self):
        subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell=True)


    def update_r1_underpopulation(self, board):    
#         (rows,cols) = np.shape(self.gol.board)
#         for x in range(0,rows)
#             for y in range(0,cols)
#                 count_neighbours()
        #Any live cell with fewer than two live neighbours dies, as if caused by under-population.
        return board
    
    def update_r2_survivors(self):
        #Any live cell with two or three live neighbours lives on to the next generation.
        pass
    
    def update_r3_crowding(self):
        #Any live cell with more than three live neighbours dies, as if by overcrowding.
        pass
        
    def update_r4_reproduction(self):
        #Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        pass
    
    
