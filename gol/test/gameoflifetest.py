import unittest
from gol.gameoflife import gameoflife
import numpy as np




class Test(unittest.TestCase):

    def boardtest(self, expected_board, new_board):
        print "Exp"
        print expected_board
        print "New"
        print new_board
        
        (exp_rows,exp_cols) = np.shape(new_board)
        (rows,cols) = np.shape(new_board)
        assert (exp_rows == rows)
        assert (exp_cols == cols)    
    
        for x in range(0,rows):
            for y in range(0,cols):
                self.assertEqual(new_board[x][y], expected_board[x][y], "Board not updated correctly at (" + str(x) + "," + str(y)+")." )
         
#    def testRun(self):
#        gol = gameoflife()
#        gol.run()
        
    def testshouldhandlefirstruleofgol(self):
        board =         [['1', '0', '0','1'], ['1', '1', '0','0'], ['0', '0', '0','0'],['0', '0', '1','1']]
        expected_board= [['1', '0', '0','0'], ['1', '1', '0','0'], ['0', '0', '0','0'],['0', '0', '0','0']]
        gol = gameoflife()
        new_board = gol.update_r1_underpopulation(board)
        self.boardtest(expected_board,new_board)
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()