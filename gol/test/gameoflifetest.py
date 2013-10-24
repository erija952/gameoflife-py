import unittest
from gol.gameoflife import gameoflife
from gol.test.testutils import boardtest
import mock
from mock import MagicMock

class Test(unittest.TestCase):
 
    def setUp(self):
        self.gol = gameoflife()
        self.board =         [['1', '0', '0','1'], ['1', '1', '0','0'], ['1', '0', '0','0'],['0', '0', '1','1']]
        self.expected_board= [['1', '1', '0','0'], ['1', '1', '0','0'], ['1', '0', '1','0'],['0', '0', '0','0']]
        self.correctlocationfrommaponfile = '/home/eral/workspace/gameoflife-py/gol/test/miniboard.txt'
        pass

    def tearDown(self):
        pass
    
#     def testRun(self):
#         gol = gameoflife()
#         gol.main()

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
        boardtest(self.expected_board,new_board)
#         
    def testShouldCreateRandomBoardIfNotGivenFile(self):        
        gol = gameoflife()
        gol.create_board = MagicMock()
        gol.enter_loop = MagicMock()
        gol.main('random','')
        gol.create_board.assert_called_once_with('random','')
        gol.enter_loop.assert_called_once_with()
    
    def testShouldCreateSpecificBoardIfCorrectFileGiven(self):        
        gol = gameoflife()
        gol.create_board = MagicMock()
        gol.enter_loop = MagicMock()
        
        gol.main('fromfile', self.correctlocationfrommaponfile)
        gol.create_board.assert_called_once_with('fromfile', self.correctlocationfrommaponfile)       
    
    def testShouldCreateCorrectBoardIfGivenAValidFile(self):
        expectedBoard =         [['0', '1', '1','0','0'], ['0', '1', '1','0','0'], ['0', '0', '0','0','1'],['0', '0', '0','1','0'],['0', '1', '1','0','0']]
        gol = gameoflife()
        gol.enter_loop = MagicMock()
        gol.main('fromfile', self.correctlocationfrommaponfile)
        gol.enter_loop.assert_called_once_with()      
        boardtest(gol.board,expectedBoard)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()