from gol.outputformater import outputformater
import gameoflifeboard
import platform
import subprocess
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
