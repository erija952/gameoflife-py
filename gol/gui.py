#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from gol.gameoflifeboard import gameoflifeboard
from gol.gameoflife import gameoflife
from os import path

class GameOfLifeGui(QtGui.QMainWindow):
    
    def __init__(self):
        super(GameOfLifeGui, self).__init__()

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('GameOfLife')
        self.GuiBoard = Board(self)
        self.center()

        self.setCentralWidget(self.GuiBoard)

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)


class Board(QtGui.QFrame):
    board = []
    rows = 0
    cols = 0
    boxsize = 10
    speed = 300
    gol = None
    
    def __init__(self, parent):
        super(Board, self).__init__()
        
        golb = gameoflifeboard()
        self.gol = gameoflife()
        
        self.board = golb.populateFromFile(path.dirname(__file__) +'/../tests/glider.txt')
        self.rows = len(self.board)
        self.cols = len(self.board[1])
        
        self.timer = QtCore.QBasicTimer()        
        self.show()
        
        self.timer.start(self.speed, self)
        
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawBoard(qp)
        qp.end()
        
    def drawBoard(self, qp):
        for y_map_index in range(0,self.rows):
            for x_map_index in range(0,self.cols):
                self.drawRectangles(qp,y_map_index,x_map_index)
        
    def drawRectangles(self, qp, y_map_index, x_map_index):
      
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)

        if self.board[y_map_index][x_map_index] == '1':
            qp.setBrush(QtGui.QColor(0, 0, 0))
            qp.drawRect(x_map_index*self.boxsize, y_map_index*self.boxsize, self.boxsize, self.boxsize)    
        else:
            qp.setBrush(QtGui.QColor(255, 255, 255, 160))
            qp.drawRect(x_map_index*self.boxsize, y_map_index*self.boxsize, self.boxsize, self.boxsize)
                
    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            new_board = self.gol.update_board(self.board)
            self.board = new_board
        else:
            QtGui.QFrame.timerEvent(self, event)

#         
#     def drawSquare(self, painter, x, y, shape):
#         
#         colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
#                       0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
# 
#         color = QtGui.QColor(colorTable[shape])
#         painter.fillRect(x + 1, y + 1, self.squareWidth() - 2, 
#             self.squareHeight() - 2, color)
# 
#         painter.setPen(color.lighter())
#         painter.drawLine(x, y + self.squareHeight() - 1, x, y)
#         painter.drawLine(x, y, x + self.squareWidth() - 1, y)
# 
#         painter.setPen(color.darker())
#         painter.drawLine(x + 1, y + self.squareHeight() - 1,
#             x + self.squareWidth() - 1, y + self.squareHeight() - 1)
#         painter.drawLine(x + self.squareWidth() - 1, 
#             y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)

def main():
    
    app = QtGui.QApplication(sys.argv)
    t = GameOfLifeGui()
    t.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
