#!/usr/bin/python
from random import randrange

class gameoflifeboard(object):

    def __init__(self):
        pass
    
    def populateFromFile(self, filename):
   
        def read_file(a):
            lines = [line.strip() for line in open(filename)]
            return lines

        board = []
        for i in read_file(filename):
            new_string = i.split(',') 
            board.append(new_string)

        return board

    
    def populateRandomly(self,x_size=10, y_size=10, ratio=0.5):
        if ratio > 1 or ratio < 0:
            raise ValueError
        
        board = []
        for x in range(0,x_size):  # @UnusedVariable
            board.append(["0"] * y_size)
        
        num_ones_set = 0        
        while num_ones_set < int(x_size * y_size * ratio):
            x = randrange(0, x_size)
            y = randrange(0, y_size)
            
            if board[x][y] != '1':
                board[x][y] = '1'
                num_ones_set += 1

        return board
                