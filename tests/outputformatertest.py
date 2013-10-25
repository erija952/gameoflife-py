import unittest
from gol.outputformater import outputformater
from StringIO import StringIO

class Test(unittest.TestCase):


    def testShouldFormatOutputCorrectlyWithCustomFormating(self):
        of = outputformater('X','.')
        board = [['0', '1', '0','1'], ['1', '0', '1','1'], ['0', '0', '1','1']]
      
        outStreamObj = StringIO()
        of.output(board, out= outStreamObj)
        printed = outStreamObj.getvalue().strip()
        
        expected = '.X.X\nX.XX\n..XX'
        self.assertEqual(printed, expected , "Output should be formatted")

    
    def testShouldFormatOutputCorrectlyCustomDelimiters(self):
        #todo: fix space as delimiter!
        of = outputformater('.','-')
        board = [['0', '1', '0','1']]
       
        outStreamObj = StringIO()
        of.output(board, out= outStreamObj)
        printed = outStreamObj.getvalue().strip()
        expected = '-.-.'
        self.assertEqual(printed, expected , "Output should be formatted")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testShouldFormatOutputCorrectly']
    unittest.main()