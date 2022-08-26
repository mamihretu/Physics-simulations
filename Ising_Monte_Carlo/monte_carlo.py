import turtle
import numpy as np
import time





def deltaU(i,j,dipoles):
    """A function to calculate energy change when flipping specified dipole"""
    size = len(dipoles)-1

    if i == 1:
        top = dipoles[size][j].state
    else:
        top = dipoles[i-1][j].state

    if i == size:
        bottom = dipoles[i][j].state
    else:
        bottom = dipoles[i+1][j].state

    if j == 1:
        left = dipoles[i][size].state
    else:
        left = dipoles[i][j-1].state

    if j == size:
        right = dipoles[i][j].state
    else:
        right = dipoles[i][j+1].state

    Ediff = 2*dipoles[i][j].state*(top+bottom+left+right)

    return Ediff

def update_dipoles(dipoles):
    """metropolis algorithm to update the state and color of dipoles"""
    global running 

    start = time.time()
    T = 2.5
    size = len(dipoles) 
    for i in range(100*size):
        rand = np.random.rand()
        x = int(np.random.randint(size-1))
        y = int(np.random.randint(size-1))

        Ediff = deltaU(x,y,dipoles)
        if Ediff <= 0:
            dipoles[x][y].state = -dipoles[x][y].state
            dipoles[x][y].set_color(dipoles[x][y].state)
        elif rand < np.exp(-Ediff/T):
            dipoles[x][y].state = -dipoles[x][y].state
            dipoles[x][y].set_color(dipoles[x][y].state)
        
        if running == False:
            break

        wn.update()
    
    finish= time.time()
    time_elapsed = finish - start
    # time elapsed
    print("done in :", time_elapsed)









    
     







