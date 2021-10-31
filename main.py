"""
I'm only 17 so please don't judge HAHA
follow me on instagram btw @tibofordeyn._
"""
import pygame as pg
import sys
from random import randint as rd
pg.init()



#   PROMINENT INITIALS - SCREEN
SCREENWIDTH = 864
SCREENHEIGHT = 1200
SCREEN = pg.display.set_mode((SCREENWIDTH,SCREENHEIGHT))


#   PROMINENT INITIALS - FRAME RATE
CLOCK = pg.time.Clock()
FPS = 120
FRAMESAM = 0


#   IMAGES - BACKGROUNDS
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
RANDBACK = rd(0,len(BACKGROUNDS)-1)


#   MAKING BIRDS
DOWNFLAP = 0
MIDFLAP = 1
UPFLAP = 2

FLAPINDEX = 0   # Will be used in a loop to make wings flap

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
BEFOREY = (
    (
        float(RECT_BIRDS[0][DOWNFLAP].centery),
        float(RECT_BIRDS[0][MIDFLAP].centery),
        float(RECT_BIRDS[0][UPFLAP].centery),
    ),
    (
        float(RECT_BIRDS[1][DOWNFLAP].centery),
        float(RECT_BIRDS[1][MIDFLAP].centery),
        float(RECT_BIRDS[1][UPFLAP].centery),
    ),
)
HIGHEST_BINDEX = len(BIRDS)-1    # Amount of birds-1 (cuz index count starts at 0)
RANDBIRD = rd(0, HIGHEST_BINDEX)

# CREATING GRAVITY UPON THE BIRD
BIRD_MOVEMENT = 0
GRAVITY = 0.1
UPWITHSPACE = 200
DOWNSPACE = UPWITHSPACE/2


#   CREATING A FLOOR
FLOORSIZE = (
    int(SCREENWIDTH),
    int(SCREENHEIGHT/5),
)
FLOORSURFACE = (
    pg.image.load("images/floors/base.png").convert(),
)
SCALEDFLOOR = (
    pg.transform.scale(FLOORSURFACE[0],(FLOORSIZE[0],FLOORSIZE[1])),
)


#   STARTING THE GAME
while True:

    pg.display.set_caption("Flappy bird voor mijn AI")
    for event in pg.event.get():

            #   MAKING CLOSING TE PROGRAM POSSIBLE
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_d):
            pg.quit()
            sys.exit()


            #   TAKING KEYBOARD INPUT
        elif event.type == pg.KEYDOWN and (event.key == pg.K_SPACE or event.key == pg.K_UP):
            RECT_BIRDS[0][DOWNFLAP].centery -= UPWITHSPACE
            RECT_BIRDS[0][MIDFLAP].centery -= UPWITHSPACE
            RECT_BIRDS[0][UPFLAP].centery -= UPWITHSPACE

            RECT_BIRDS[1][DOWNFLAP].centery -= UPWITHSPACE
            RECT_BIRDS[1][MIDFLAP].centery -= UPWITHSPACE
            RECT_BIRDS[1][UPFLAP].centery -= UPWITHSPACE

            if RANDBIRD == HIGHEST_BINDEX:  # Will make the bird change colors
                RANDBIRD -= HIGHEST_BINDEX # Resets to 0
            elif RANDBIRD != HIGHEST_BINDEX:
                RANDBIRD += 1
    
                
        elif event.type == pg.KEYDOWN and (event.key == pg.K_DOWN):
            RECT_BIRDS[0][DOWNFLAP].centery += DOWNSPACE
            RECT_BIRDS[0][MIDFLAP].centery += DOWNSPACE
            RECT_BIRDS[0][UPFLAP].centery += DOWNSPACE

            RECT_BIRDS[1][DOWNFLAP].centery += DOWNSPACE
            RECT_BIRDS[1][MIDFLAP].centery += DOWNSPACE
            RECT_BIRDS[1][UPFLAP].centery += DOWNSPACE

            if RANDBIRD == HIGHEST_BINDEX:  # Will make the bird change colors
                RANDBIRD -= HIGHEST_BINDEX # Resets to 0
            elif RANDBIRD != HIGHEST_BINDEX:
                RANDBIRD += 1
          

    #   CHOOSING AND BLITTING A BACKGROUND
    SCREEN.blit(SCALED_BACKGROUNDS[RANDBACK],(0,0))


    #   CHOOSING AND BLITTING A BIRD + BIRD GRAVITY
    if FRAMESAM%10==0:
        if FLAPINDEX < 2:
            FLAPINDEX += 1
        else:
            FLAPINDEX = 0

    BIRD_MOVEMENT += GRAVITY
    

    SCREEN.blit(SCALED_BIRDS[RANDBIRD][FLAPINDEX], RECT_BIRDS[RANDBIRD][FLAPINDEX])


    #   CHOOSING AND BLITTING A SURFACE
    SCREEN.blit(SCALEDFLOOR[0], (0,960))


    #   UPDATING DISPLAY AFTER EACH LOOP + SPEED OF ITERATION
    pg.display.update()
    CLOCK.tick(FPS)
    FRAMESAM += 1
