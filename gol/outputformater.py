#!/usr/bin/python
import sys

class outputformater(object):

    def __init__(self, occupied = 'X', unoccupied = '_'):
        self.occupied = occupied
        self.unoccupied = unoccupied     
        pass
    
    def output(self, board, out=sys.stdout):
        nstring = ''
        for col in board:
            stringified = "".join(col)
            string = stringified.replace('1', self.occupied)
            nstring = nstring + string.replace('0', self.unoccupied)
            nstring = nstring + "\n"
        
        out.write(nstring)   
    