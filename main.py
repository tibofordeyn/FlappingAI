'''
As you can see in my first commit, I initially didn't realise that
my code would have to be object oriented.

I now realise I'll have to write this code using 3 classes:
    1 for the birds
    1 for the pipes
    and 1 more for the floor
'''

import pygame as pg 
from random import randint as rd 
from os import sys
import neat
import time
pg.init()


#   STATIC INITIALS - SCREEN
SCREENWIDTH = 864
SCREENHEIGHT = 1200
SCREEN = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT))


#   STATIC INITIALS - CLOCK
CLOCK = pg.time.Clock()
FPS = 120
FRAMESAM = 0


#   STATIC INITIALS - BACKGROUNDS + BACKGROUND DISPLAY
BACKGROUNDS = (
        pg.image.load("images/backgrounds/background-day.png").convert(),
        pg.image.load("images/backgrounds/background-night.png").convert(),
        pg.image.load("images/backgrounds/MarioBackground-static.png").convert(),
        pg.image.load("images/backgrounds/spacebg.png").convert(),
)
SCALED_BACKGROUNDS = (
    pg.transform.scale(BACKGROUNDS[0],(SCREENWIDTH, SCREENHEIGHT)),
    pg.transform.scale(BACKGROUNDS[1],(SCREENWIDTH, SCREENHEIGHT)),
    pg.transform.scale(BACKGROUNDS[2],(SCREENWIDTH, SCREENHEIGHT)),
    pg.transform.scale(BACKGROUNDS[3],(SCREENWIDTH, SCREENHEIGHT)),
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
    pg.transform.scale(FLOORSURFACE[0],(FLOORSIZE[0],FLOORSIZE[1])),
)
RECT_FLOORS = (
    SCALED_FLOORS[0].get_rect(left = 0, right = SCREENHEIGHT)
)
FHIGHEST_INDEX = len(FLOORS)-1
RANDFLOOR = rd(0,FHIGHEST_INDEX)
"""
The RANDFLOOR will be used to generate a new floor for
every 5 points. It will change at the same time as the 
background.
"""

