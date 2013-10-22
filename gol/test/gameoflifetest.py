import unittest
from gol.gameoflife import gameoflife

class Test(unittest.TestCase):


    def testName(self):
#         gol = gameoflife()       
#         gol.update()
#         self.assertEqual()
        gol = gameoflife()
        gol.run()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()