



import turtle
import numpy as np
import time



#custom Turtle class to create dipoles 
class Dipole():

    def __init__(self, x_cor = None, y_cor = None , wid_stretch = None, len_stretch = None, color = "black", state = 0, shape = "square" ):
        self.dipole = turtle.Turtle()
        self.shape = self.dipole.shape(shape)
        self.color = self.dipole.color(color)
        self.shapesize = self.dipole.shapesize(stretch_wid = wid_stretch , stretch_len = len_stretch)
        self.state = state
        self.dipole.penup()
        self.dipole.goto(x_cor, y_cor)


    def clear(self):
        self.dipole.clear()

    def xcor(self):
        return self.dipole.xcor()  

    def ycor(self):
        return self.dipole.ycor() 
    def set_color(self, state):
        if state == -1:
            self.dipole.color("white")
        elif state == 1:
            self.dipole.color("black")
        else:
            print("state must be either +1 or -1")





# A function to create dipoles and append them to a list

def create_dipoles(number_of_rows, window_width):
    dipole_list = []
    for i in range(number_of_rows):
        y = []
        dipole_list.append(y)

    
    end_point = int(window_width/2)
    step = int(window_width/number_of_rows)
    start_point = int((step/2) - end_point)
    dipole_size = step/20

    x = 0
    y = 0
    for i in range(start_point, end_point, step):
        for j in range(start_point, end_point, step):
            color_list = ["black","white"]
            c = np.random.randint(2)
            if c == 0:
                dipole_list[x].append(Dipole(i,j,dipole_size,dipole_size, color=color_list[c], state = 1))
            else:
                dipole_list[x].append(Dipole(i,j,dipole_size,dipole_size, color=color_list[c], state = -1))

            y+=1
        x+=1

    return dipole_list




# A function to calculate energy change when flipping specified dipole

def deltaU(i,j,dipoles):
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



# metropolis algorithm to update the state and color of dipoles

def update_dipoles(dipoles):
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






# create and initialize window with specified parameters

Width = 600 
Height = 600

wn = turtle.Screen()
wn.title("monte_carlo_ising_model")
wn.bgcolor("black")
wn.setup(width=Width, height= Height)
wn.tracer(0)


# get root canvas to properly close the window

canvas = wn.getcanvas()  # or, equivalently: turtle.getcanvas()
root = canvas.winfo_toplevel()

def on_close():
    global running
    running = False

root.protocol("WM_DELETE_WINDOW", on_close)
running = True  



# create dipoles 

number_of_rows = 10
window_size = Width
dipoles = create_dipoles(number_of_rows,window_size)





# main gui loop 

update_dipoles(dipoles)
while running == True:

    if running == False:
        break
    wn.update


    
     







