import turtle
import numpy as np
import time





def create_dipoles(number_of_rows, window_width):
    """A function to create dipoles and append them to a list"""
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


def run():
	"""create and initialize window with specified parameters"""

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
	    wn.update# 




if "__name__" == "__main__":
	run()