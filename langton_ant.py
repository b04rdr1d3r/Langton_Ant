################################################################################################
# a simple Langton's ant simulation
# (c) JP Darsonville 2019
# GPL v3
################################################################################################

# handle dependencies

import pygame
import time
import sys

# constants are declared below
MAX_X = 300
MAX_Y = 300
OFFSET_X = 5
OFFSET_Y = 5
MAX_GEN = 15000
SCALE = 2
N = 1
E = 2
S = 3
O = 4
direc = 1

# window parameters
background_colour = (255,255,255)
foreground_color = (0,0,0)
##width = (MAX_X + OFFSET_X * 2) * SCALE
##height = (MAX_Y + OFFSET_Y * 2) * SCALE
width = (MAX_X + 1) * SCALE
height = (MAX_Y + 1) * SCALE

# used for increments
i = 0
j = 0
gen = 0

# create the grid
grid = [ [ 0 for i in range(0, MAX_X + 1) ] for j in range(0, MAX_Y + 1) ]
# place the ant at the center
x = int(MAX_X / 2) + 1
y = int(MAX_Y / 2) + 1

################################################################
#  plots output on the screen based on input coordinates
################################################################
def plot (x, y, color):
    if color == 1:
        sel_color = (0,0,0)
    else:
        sel_color = (255,255,255)
    pygame.draw.rect(screen, sel_color, [(x)* SCALE, (y) * SCALE, SCALE, SCALE])



def turn_right(old_direc):
    if old_direc == O:
        new_direc = N
    else:
        new_direc = old_direc + 1
    return new_direc



def turn_left(old_direc):
    if old_direc == N:
        new_direc = O
    else:
        new_direc = old_direc - 1
    return new_direc


# open window and populate start grid
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fourmi de Langton by JP Darsonville')
screen.fill(background_colour)
pygame.display.flip()

# phase 2 - begin game and increment from the planned number of generations
for gen in range(1, MAX_GEN):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ## move_ant ##
    if grid[x][y] == 1:
        direc = turn_left(direc)
        grid[x][y] = 0
    else:
        direc = turn_right(direc)
        grid[x][y] = 1
    if direc == N:
        y = y - 1
    elif direc == E:
        x = x + 1
    elif direc == S:
        y = y + 1
    elif direc == O:
        x = x - 1
    else:
        print("erreur:" + str(direc))
        sys.exit()

    ################
    #print (direc,x,y, grid[x][y])

    pygame.display.set_caption('Generation:' + str(gen))
    plot(x, y, grid[x][y])
    pygame.display.flip()
    #time.sleep(1.5)

# end simulation / wait for user input to remove grid
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

# end program
