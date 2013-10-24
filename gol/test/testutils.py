import numpy as np

def boardtest(expected_board, new_board):
    (exp_rows,exp_cols) = np.shape(new_board)
    (rows,cols) = np.shape(new_board)
    assert (exp_rows == rows)
    assert (exp_cols == cols)    
    
    for y in range(0,rows):
        for x in range(0,cols):
            print "(y,x)=("+str(y)+","+str(x)+")"            
            assert new_board[y][x] == expected_board[y][x]