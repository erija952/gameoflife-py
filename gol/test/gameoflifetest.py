import unittest
from gol.gameoflife import gameoflife
import numpy as np

class Test(unittest.TestCase):
 
    def setUp(self):
        self.gol = gameoflife()
        self.board =         [['1', '0', '0','1'], ['1', '1', '0','0'], ['1', '0', '0','0'],['0', '0', '1','1']]
        self.expected_board= [['1', '1', '0','0'], ['1', '1', '0','0'], ['1', '0', '1','0'],['0', '0', '0','0']]
        pass

    def tearDown(self):
        pass
    
    def boardtest(self, expected_board, new_board):
        (exp_rows,exp_cols) = np.shape(new_board)
        (rows,cols) = np.shape(new_board)
        assert (exp_rows == rows)
        assert (exp_cols == cols)    
    
        for x in range(0,rows):
            for y in range(0,cols):
                self.assertEqual(new_board[y][x], expected_board[y][x], "Board not updated correctly at (" + str(x) + "," + str(y)+")." )
         
#     def testRun(self):
#         gol = gameoflife()
#         gol.run()

    def testcountneighbours(self):
        self.assertEqual(self.gol.count_neighbours(0,0,self.board), 2, "Should give correct number of neighbours")
        self.assertEqual(self.gol.count_neighbours(1,0,self.board), 3, "Should give correct number of neighbours")
        self.assertEqual(self.gol.count_neighbours(3,1,self.board), 2, "Should give correct number of neighbours")
        self.assertEqual(self.gol.count_neighbours(1,1,self.board), 3, "Should give correct number of neighbours")
        self.assertEqual(self.gol.count_neighbours(3,3,self.board), 1, "Should give correct number of neighbours")
               
    def testwheterlivecellshouldsurvivetonextgeneration(self):
        '''Any live cell with fewer than two live neighbours dies, as if caused by under-population.
        Any live cell with two or three live neighbours lives on to the next generation.    
        Any live cell with more than three live neighbours dies, as if by overcrowding.'''
        self.assertFalse(self.gol.live_cell_survives_to_next_generation_r1r2r3(0), "Live cell with X neighbours should not survive to next generation")
        self.assertFalse(self.gol.live_cell_survives_to_next_generation_r1r2r3(1), "Live cell with X neighbours should not survive to next generation")
        self.assertTrue(self.gol.live_cell_survives_to_next_generation_r1r2r3(2), "Live cell with X neighbours should survive to next generation")
        self.assertTrue(self.gol.live_cell_survives_to_next_generation_r1r2r3(3), "Live cell with X neighbours should survive to next generation")
        self.assertFalse(self.gol.live_cell_survives_to_next_generation_r1r2r3(4), "Live cell with X neighbours should not survive to next generation")
        
    def testwheterdeadcellshouldsurvivetonextgeneration(self):
        '''Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.'''
        self.assertFalse(self.gol.dead_cell_resurrects_r4(0), "Dead cell with X neighbours should not come to life")
        self.assertFalse(self.gol.dead_cell_resurrects_r4(1), "Dead cell with X neighbours should not come to life")
        self.assertTrue(self.gol.dead_cell_resurrects_r4(3), "Dead cell with X neighbours should not come to life")
        self.assertFalse(self.gol.dead_cell_resurrects_r4(4), "Dead cell with X neighbours should not come to life")
        
    def testupdateboardaccordingtorules(self):
        new_board = self.gol.update_board(self.board)       
        self.boardtest(self.expected_board,new_board)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()