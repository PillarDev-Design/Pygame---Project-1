# BEGIN DATE:  8/27/2011
# FINISH DATE: x/xx/xxxx
# Source material derived from http://inventwithpython.com/chapter18.html

# FILE NAME: Project1.py
# DESCRIPTION: This project is designed to combine the principles of frame by
#     frame animation along with user input controls. This will incorporate
#     importing PNG's and slicing their frames into an array.

# *** IMPORT CODE ***
import pygame, sys, random
from pygame.locals import *
# *** END IMPORT CODE ***

# *** CLASS CODE ***
# --- Main Character Class Sprite ---
class Character(pygame.sprite.Sprite):
    # Initial Coordinates
    posX = 200
    posY = 200
    # Code when the class initializes
    def __init__(self,img,frames=1,modes=1,width=32,height=32,fps=3):
        # Init the sprite
        pygame.sprite.Sprite.__init__(self)
        # Capture the full size of the imported PNG
        original_width, original_height = img.get_size()
        # Declare the width, height, and number of frames
        self._w = width
        self._h = height
        self._framelist = []
        # Slice up the frames from the imported PNG
        for i in xrange(int(original_width/width)):
            self._framelist.append(img.subsurface((i*width,0,width,height)))
        # Set the current image as the first in the framelist
        self.image = self._framelist[0]
        # Set the current frame as 0
        self._frame = 0
        # Begin tracking time when we began to know when to switch the frame
        self._start = pygame.time.get_ticks()
        # Calculate delay with fps
        self._delay = 1000 / fps
        # Clear and declare the last update
        self._last_update = 0
        # The following links with the class function call update
        # Parameters (time, width, height) 
        # self.update(pygame.time.get_ticks(), 100, 100)

    # Set position function
    def set_pos(self,x,y):
        self.posX = x
        self.posY = y
    # Get position function
    def get_pos(self):
        return(self.posX,self.posY)

    # This function computes the inputs and cmputes where the
    #     character should be
    # The width and height called in this function are the
    #     SCREEN_W, SCREEN_H
    def update(self,t,width,height,moveDict):
        # Calculate movement
        if moveDict['moveDown'] and ((self.posY + self._h) < height):
            self.posY += moveDict['MOVESPEED'] 
        if moveDict['moveUp'] and self.posY > 0:
            self.posY -= moveDict['MOVESPEED']
        if moveDict['moveRight'] and ((self.posX + self._w) < width):
            self.posX += moveDict['MOVESPEED']
        if moveDict['moveLeft'] and self.posX > 0:
            self.posX -= moveDict['MOVESPEED']
        # Calculate frame flip
        
        if moveDict['movement']:
            if t - self._last_update > self._delay:
                self._frame += 1
                if self._frame >= len(self._framelist):
                    self._frame = 0
                self.image = self._framelist[self._frame]
                self._last_update = t
        
# *** END CLASS CODE ***

# *** MAIN FUNCTION ***
def main():
    # *** DECLARE CONSTANTS/VARIABLES ***
    SCREEN_W = 300
    SCREEN_H = 300
    moveDict = {
        'moveLeft':False,
        'moveRight':False,
        'moveUp':False,
        'moveDown':False,
        'MOVESPEED':3,
        'movement':False
        }
    # *** END CONSTANT/VARIABLE CODE ***
    
    # Perform inits
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W,SCREEN_H),0,32)
    pygame.display.set_caption('Pillar DD: Project 1')

    # Load PNG's
    background = pygame.image.load('resources/field.png')
    img_orc = pygame.image.load('resources/orc.png')
    
    # Create instance of class with the following paramters specified above
    # Target_Image, Total Frames, Modes, Width, Height, FPS (Optional, set at 3)
    orc = Character(img_orc, 4, 1, 32, 48, 3)

    # Game Loop
    while True:
        # Define keystrokes
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord('a'):
                    moveDict['moveRight'] = False
                    moveDict['moveLeft'] = True
                    moveDict['movement'] = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveDict['moveLeft'] = False
                    moveDict['moveRight'] = True
                    moveDict['movement'] = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDict['moveDown'] = False
                    moveDict['moveUp'] = True
                    moveDict['movement'] = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDict['moveUp'] = False
                    moveDict['moveDown'] = True 
                    moveDict['movement'] = True
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT or event.key == ord('a'):
                    moveDict['moveLeft'] = False
                    moveDict['movement'] = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveDict['moveRight'] = False
                    moveDict['movement'] = False
                if event.key == K_UP or event.key == ord('w'):
                    moveDict['moveUp'] = False
                    moveDict['movement'] = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDict['moveDown'] = False
                    moveDict['movement'] = False
        # Now to render everything
        screen.blit(background,(0,0))
        screen.blit(orc.image,orc.get_pos())
        # Update the orc input
        orc.update(pygame.time.get_ticks(),SCREEN_W,SCREEN_H,moveDict)
        # Update the display
        pygame.display.update()
        # Delay
        pygame.time.delay(10)

if __name__ == '__main__': main()
