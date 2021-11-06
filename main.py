'''
As you can see in my first commit, I initially didn't realise that
my code would have to be object oriented.

I now realise I'll have to write this code using 3 classes:
    1 for the birds
    1 for the pipes
    and 1 more for the floor
'''


import pygame as pg 
from random import randint as rd, randrange as rdr
from os import sys
import neat as nt
import time as tm
pg.init()


#   STATIC INITIALS - SCREEN
SCREENWIDTH = 864
SCREENHEIGHT = 1200
SCREEN = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pg.display.set_caption("AI  PLAYS  FLAPPY  BIRD !")


#   STATIC INITIALS - CLOCK
CLOCK = pg.time.Clock()
FPS = 120
FRAMESAM = 0


#   STATIC INITIALS - MOVEMENT
BIRDJUMP = -200


#   STATIC INITIALS - BACKGROUNDS + BACKGROUND DISPLAY
BACKGROUNDS = (
        pg.image.load("images/backgrounds/background-day.png").convert(),
        pg.image.load("images/backgrounds/background-night.png").convert(),
        pg.image.load("images/backgrounds/MarioBackground-static.png").convert(),
        pg.image.load("images/backgrounds/spacebg.png").convert(),
        pg.image.load("images/backgrounds/underwater.jpeg").convert(),
)
SCALED_BACKGROUNDS = (
    pg.transform.scale(BACKGROUNDS[0],(SCREENWIDTH, SCREENHEIGHT)),
    pg.transform.scale(BACKGROUNDS[1],(SCREENWIDTH, SCREENHEIGHT)),
    pg.transform.scale(BACKGROUNDS[2],(SCREENWIDTH, SCREENHEIGHT)),
    pg.transform.scale(BACKGROUNDS[3],(SCREENWIDTH, SCREENHEIGHT)),
    pg.transform.scale(BACKGROUNDS[4],(SCREENWIDTH, SCREENHEIGHT)),
)
BAHIGHEST_INDEX = len(BACKGROUNDS)-1
RANDBACK = rd(0,BAHIGHEST_INDEX)
"""
The randback variable choses an index for which background to 
display. There will be a different background displayed for
every 5 points.
"""


#   STATIC INITIALS - BIRDS + BIRD DISPLAY
DOWNFLAP = 0
MIDFLAP = 1
UPFLAP = 2
FLAPINDEX = 0
BIRDPOS = (
    SCREENWIDTH/4,
    SCREENHEIGHT/2,
)
BIRDSSIZE = (
    int(SCREENWIDTH/10),
    int(SCREENHEIGHT/20),
)
BIRDS = (
    (
        pg.image.load("images/birds/bluebird-downflap.png").convert(),
        pg.image.load("images/birds/bluebird-midflap.png").convert(),
        pg.image.load("images/birds/bluebird-upflap.png").convert(),
    ),
    (
        pg.image.load("images/birds/redbird-downflap.png").convert(),
        pg.image.load("images/birds/redbird-midflap.png").convert(),
        pg.image.load("images/birds/redbird-upflap.png").convert(),
    ),
)
SCALED_BIRDS = (
    (
    pg.transform.scale(BIRDS[0][DOWNFLAP], (BIRDSSIZE[0],BIRDSSIZE[1])),
    pg.transform.scale(BIRDS[0][MIDFLAP], (BIRDSSIZE[0],BIRDSSIZE[1])),
    pg.transform.scale(BIRDS[0][UPFLAP], (BIRDSSIZE[0],BIRDSSIZE[1])),
    ),
    (
    pg.transform.scale(BIRDS[1][DOWNFLAP], (BIRDSSIZE[0],BIRDSSIZE[1])),
    pg.transform.scale(BIRDS[1][MIDFLAP], (BIRDSSIZE[0],BIRDSSIZE[1])),
    pg.transform.scale(BIRDS[1][UPFLAP], (BIRDSSIZE[0],BIRDSSIZE[1])),
    ),
)
RECT_BIRDS = (
    (
    SCALED_BIRDS[0][DOWNFLAP].get_rect(center = (BIRDPOS[0],BIRDPOS[1])),
    SCALED_BIRDS[0][MIDFLAP].get_rect(center = (BIRDPOS[0],BIRDPOS[1])),
    SCALED_BIRDS[0][UPFLAP].get_rect(center = (BIRDPOS[0],BIRDPOS[1])),
    ),
    (
    SCALED_BIRDS[1][DOWNFLAP].get_rect(center = (BIRDPOS[0],BIRDPOS[1])),
    SCALED_BIRDS[1][MIDFLAP].get_rect(center = (BIRDPOS[0],BIRDPOS[1])),
    SCALED_BIRDS[1][UPFLAP].get_rect(center = (BIRDPOS[0],BIRDPOS[1])),
    ),
)
BHIGHEST_INDEX = len(BIRDS)-1
RANDBIRD = rd(0, BHIGHEST_INDEX)
"""
The flapindex will be used in the function to make the bird
flap its wings.
RECT_BIRDS will have the images of the birds, scaled, and 
gives them a position on the screen. That position is determined
in the BIRDPOS list.
HIGHEST_BINDEX is the highest index in the birds list.
RANDBIRD will be used to randomly choose which bird to display.
"""


#   STATIC INITIALS - THE FLOOR
FLOORSIZE = (
    int(SCREENWIDTH),
    int(SCREENHEIGHT/5),
)
FLOORS = (
    pg.image.load("images/floors/base.png").convert(),
)
SCALED_FLOORS = (
    pg.transform.scale(FLOORS[0],(FLOORSIZE[0],FLOORSIZE[1])),
)
RECT_FLOORS = (
    SCALED_FLOORS[0].get_rect(left = 0, right = SCREENHEIGHT)
)
FHIGHEST_INDEX = len(FLOORS)-1
RANDFLOOR = rd(0,FHIGHEST_INDEX)
"""
- The RANDFLOOR will be used to generate a new floor for
every 5 points. It will change at the same time as the 
background.
"""


#   STATIC INITIALS - PIPES + PIPES DISPLAY
PIPES = (
    pg.image.load("images/pipes/groenePijp.png").convert(),
    pg.image.load("images/pipes/rodePijp.png").convert(),
)
SCALED_PIPES = (
    pg.transform.scale2x(PIPES[0]),
    pg.transform.scale2x(PIPES[1]),
)
PHIGHEST_INDEX = len(PIPES)-1
RANDPIPE = rd(0,PHIGHEST_INDEX)
STARTPOS = SCREENWIDTH*1.2
"""
- These are the pipe images. The variables are
needed to make one of the 2 colored pipes appear.
"""


#   CREATING THE CLASSES - BIRDS
class Bird:

    DOWNFLAP = 0
    MIDFLAP = 1
    UPFLAP = 2
    FLAPINDEX = 0

    def __init__(self,x,y):
        """
        Initial values that will be used in the other functions
        """
        self.x = x
        self.y = y
        self.tickc = 0
        self.grav = 0
        self.height = self.y
        self.imgcount = 0
        self.imgs = SCALED_BIRDS[RANDBIRD][self.FLAPINDEX]

    def jump(self):
        self.grav = BIRDJUMP
        self.tickc = 0
        self.height = self.y

    def move(self):
        self.tickc +=1

        DISPLACEMENT = self.grav*self.tickc + 1.5*self.tickc**2
        if DISPLACEMENT >= 16:
            DISPLACEMENT = 16
        elif DISPLACEMENT < 0:
            DISPLACEMENT -=4
        self.y += DISPLACEMENT

    def toDisplay(self, screen):
        """
        This function will change the displayed image
        so that the bird flaps, except for when it is going
        down.
        """
        self.imgcount += 1
        self.imgs = SCALED_BIRDS[RANDBIRD][self.FLAPINDEX]
        DISPLACEMENT = self.grav*self.tickc + 1.5*self.tickc**2

        if self.imgcount%50==0:
            if self.FLAPINDEX < self.UPFLAP:
                self.FLAPINDEX += 1
            else:
                self.FLAPINDEX -= self.FLAPINDEX
        if DISPLACEMENT < 0:
            self.FLAPINDEX = 1

        screen.blit(self.imgs, (self.x,self.y))

    def get_prop(self):
        return pg.mask.from_surface(self.imgs)


#   CREATING THE CLASSES - PIPES
class Pipe():
    """
    - this class represents every pipe object that's
    blitted.
    """
    SCREENHEIGHT = SCREENHEIGHT
    SCREENWIDTH = SCREENWIDTH
    RANDPIPE = RANDPIPE
    PIPEGAP = 300
    SPEED = 0.7

    MINHEIGHT = 50
    MAXHEIGHT = SCREENHEIGHT/2

    def __init__(self, x):
        """
        - The topBotGap is the gap in between the 
        top and bottom of the pipe. Basically the
        area threw which the bird has to fly.
        - The self.top and self.bottom represent
        the top and bottom of pipes.
        """
        self.x = x
        self.height = 0
        self.topBotGap = 250
        self.top = 0
        self.bottom = 0

        self.imgc = 0
        self.PIPE_TOP = pg.transform.flip(SCALED_PIPES[self.RANDPIPE], False, True)
        self.PIPE_BOTTOM = SCALED_PIPES[self.RANDPIPE]

        self.passed = False
        self.move()
        self.set_height()

    def set_height(self):
        """
        - Will set a random height for the pipe.
        """
        self.height = rdr(self.MINHEIGHT, self.MAXHEIGHT)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height+self.PIPEGAP

    def move(self):
        self.x -= self.SPEED

    def toDisplay(self, screen: pg.Surface):
        """
        - Will draw the the top and bottom of the pipes.
        """
        screen.blit(self.PIPE_TOP, (self.x, self.top))
        screen.blit(self.PIPE_BOTTOM, (self.x, self.bottom))
        self.move()

        

#   PROMINENT FUNCTIONS - DRAWING THE WINDOW
def make_screen(screen, bird, pipes):
    """
    - Draws the given arguments, which are supposed
    to be sufraces, onto the big screen surface.
    - First line is for blitting the background, this
    is the big screen surface upon which all the other 
    surfaces are drawn.
    """
    screen.blit(SCALED_BACKGROUNDS[RANDBACK],(0,0))

    for pipe in pipes:
        Pipe.toDisplay(pipe, screen)
    bird.toDisplay(screen)

    pg.display.update()


#   PROMINENT FUNCTIONS - MAIN FUNCTION
def main():
    bird = Bird(BIRDPOS[0],BIRDPOS[1])
    pipes = [Pipe(STARTPOS), Pipe(STARTPOS+500)]
    SCREEN = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_d) or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

        make_screen(SCREEN, bird, pipes)








main()
