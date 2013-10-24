import unittest
import numpy as np
from gol.gameoflifeboard import gameoflifeboard
from gol.test.testutils import boardtest
        
class Test(unittest.TestCase):
 
    def setUp(self):
        self.gol = gameoflifeboard()
        pass

    def tearDown(self):
        pass
           
    def testPopulateRandomly(self):
        board = self.gol.populateRandomly(10,10,0.5)
        nr_of_ones_at_board = 0               
        for i in board: nr_of_ones_at_board += i.count('1')
        self.assertEqual(nr_of_ones_at_board, int(10*10*0.5), "Correct number of elements should be set to one")
    
    def testPopulateShouldHandleIncorrectRatio(self):     
        #todo: fix!   
#         self.assertRaises(ValueError, self.gol.populateRandomly(10,10,2))
#         self.assertRaises(ValueError, self.gol.populateRandomly(10,10,-0.1))
        pass
    
    def testLoadFromFile(self):
        board = self.gol.populateFromFile("/home/eral/workspace/gameoflife-py/gol/test/miniboard.txt")
        expectedBoard = [['0', '1', '1','0','0'], ['0', '1', '1','0','0'], ['0', '0', '0','0','1'],['0', '0', '0','1','0'],['0', '1', '1','0','0']]
        boardtest(board, expectedBoard)   
        
    def testLoadNonSquareMapFromFile(self):
        board = self.gol.populateFromFile("/home/eral/workspace/gameoflife-py/gol/test/mini-non-square.txt")
        expectedBoard = [['0', '1', '1','0','0'], ['0', '1', '1','0','0'], ['0', '0', '0','0','1'],['0', '0', '0','1','0'],['0', '1', '1','0','0'],['0', '0', '0','0','0']]
        boardtest(board, expectedBoard)           
        
                        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testShouldCreateBoard']
    unittest.main()