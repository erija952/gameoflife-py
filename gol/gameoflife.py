#!/usr/bin/python
from gol.outputformater import outputformater
import gameoflifeboard
import platform
import subprocess
import numpy as np
import sys
import argparse
import os.path

class gameoflife(object):

    def __init__(self):
        self.boardtype = 'random'
        self.filename = '' 
        self.board = []    

    def verify_input(self, boardtype, inputfile):
        if boardtype == 'fromfile':
            if os.path.isfile(inputfile):
                self.boardtype = 'fromfile'
                self.filename = inputfile
            else:
                print "Inputfile does not exist, using random board"


    def create_board(self, boardtype, filename):
        golb = gameoflifeboard.gameoflifeboard()
        if(boardtype == 'random'):
            self.board = golb.populateRandomly(20, 20, 0.5)
        else:
            self.board = golb.populateFromFile(filename)

    def enter_loop(self):
        print "Starting main loop:"        
        
        of = outputformater(u'\u25FC',u'\u25FD')
        board = self.board
        of.output(board)
        
        myinput =''
        while myinput != 'q':
            self.clear()
            board = self.update_board(board)
            
            of.output(board)
            myinput = raw_input(':')
                
    def main(self, boardtype, inputfile):
        self.verify_input(boardtype, inputfile)
        self.create_board(self.boardtype, self.filename)        
        self.enter_loop()                 
        
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
                    if curx >= 0 and curx < max_cols:
                        if cury >= 0 and cury < max_rows:
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
        for y in range(0,rows):
            for x in range(0,cols):
                nr_neighbours = self.count_neighbours(y, x, board)
                               
                if board[y][x] == '1':
                    if self.live_cell_survives_to_next_generation_r1r2r3(nr_neighbours):
                        new_board[y][x] = '1'
                else:
                    if self.dead_cell_resurrects_r4(nr_neighbours):
                        new_board[y][x] = '1'
        return new_board
    
    
    
if __name__ == '__main__':
    sys.path.append("/home/eral/workspace/gameoflife-py/gol")
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, help="location of txt file with map")
    args = parser.parse_args()
    if args.input:
        inputfile= args.input
        boardtype='fromfile'
    else:
        inputfile = ''
        boardtype='random'
    gol = gameoflife()
    gol.main(boardtype, inputfile)
    
