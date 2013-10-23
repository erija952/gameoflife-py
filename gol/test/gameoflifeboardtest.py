import unittest
import numpy as np
from gol.gameoflifeboard import gameoflifeboard
        
class Test(unittest.TestCase):
 
    def setUp(self):
        self.gol = gameoflifeboard()
        pass

    def tearDown(self):
        pass
    
    def testShouldCreateBoard(self):
        self.assertEqual(self.gol.boardInitiated, False, "Board is not initiated yet")
        self.gol.createBoard(10,10)
        self.assertEqual(self.gol.boardInitiated, True, "Board should be initiated")
        (rows,cols) = np.shape(self.gol.board)
        self.assertEqual(rows,10, "Board should have correct size")
        self.assertEqual(cols,10, "Board should have correct size")
        
        self.gol.createBoard(80,90)      
        (rows,cols) = np.shape(self.gol.board)
        self.assertEqual(rows,80, "Board should have correct size")
        self.assertEqual(cols,90, "Board should have correct size")

    def testShouldPopulateBoardDefault(self):
        self.gol.createBoard(10,10)
        self.gol.populate()    
        nr_of_ones_at_board = 0
        for i in self.gol.board: nr_of_ones_at_board += i.count('1')
        self.assertEqual(nr_of_ones_at_board, int(10*10*0.5), "Correct number of elements should be set to one")
        
    def testPopulateShouldHandleIncorrectRatio(self):        
        self.gol.createBoard(10,10)
        self.assertRaises(ValueError, self.gol.populate,1.1)
        self.assertRaises(ValueError, self.gol.populate,-0.1)
                        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testShouldCreateBoard']
    unittest.main()