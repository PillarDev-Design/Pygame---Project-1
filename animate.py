# BEGIN DATE:            Aug 27, 2011
# ALPHA COMPLETION DATE: xxx xx, xxxx
# FINAL COMPLETION DATE: xxx xx, xxxx
# FILE NAME:             animate.py
# SUBJECT:               Attempt at deciphering running_orcs
# There are numerous documentations on the web concerning
#     animation with the pygame API. All of top 10 seem
#     to be inefficient/malfunctioning. This running_orcs
#     file seems to be the only one that doesn't require
#     an additional API import. There are many ambiguous
#     variable names. This would be a good starting point
#     for any pygame tutorials I wish to write.
#                               - Chris Nabors
# Imports
import pygame, random
from pygame.locals import *
# *** BEGIN CLASS CODE ***
class Char(pygame.sprite.Sprite):
    # Initial position? Coords?
    x,y=(100,0)
    # Initialize
    # Function target self
    # Image? Image that is imported?
    # Frames? Current frame it is set on?
    # Modes???
    # Width 32px
    # Heigh 32px
    # Frames per second (3)?
    def __init__(self,img,frames=1,modes=1,w=32,h=32,fps=3):
        # Initialize the sprite
        pygame.sprite.Sprite.__init__(self)
        # ???
        original_width, original_height = img.get_size()
        # Set width, height
        self._w = w
        self._h = h
        self._framelist = []
        # Make frames from image set?
        for i in xrange(int(original_width/w)):
            self._framelist.append(img.subsurface((i*w,0,w,h)))
        # Make first frame?
        self.image = self._framelist[0]
        # Self._start?
        self._start = pygame.time.get_ticks()
        # Independent frame FPS
        self._delay = 1000 / fps
        # _last_update ??
        self._last_update = 0
        # _frame... different from self._framelist[0]???
        self._frame = 0
        # update...
        # What are the significance of these parameters....?
        self.update(pygame.time.get_ticks(),100,100)
    # Set position function
    # Pretty straight forward....
    def set_pos(self,x,y):
        self.x = x
        self.y = y
    # Get position function
    # Pretty straight forward....
    def get_pos(self):
        return (self.x,self.y)
    # Update function....
    def update(self,t,width,height):
        # Position
        # This continuously moves the character +=1
        # Moving the y coordinate +=1 will move character down
        # Y-AXIS: -=1 UP, +=1 DOWN
        # X-AXIS: -=1 LEFT, +=1 RIGHT
        self.y+=1
        if (self.y > width):
            # Not sure of this statement...
            self.x = random.randint(0,height-self._w)
            self.y = -self._h
        # Animation... flip frames?
        if t - self._last_update > self._delay:
            self._frame += 1
            if self._frame >= len(self._framelist):
                self._frame = 0
            self.image = self._framelist[self._frame]
            self._last_update = t
# *** END CLASS CODE ***

# *** DECLARE CONSTANTS ***
SCREEN_W, SCREEN_H = (320,320)
# *** END CONSTANT CODE ***

# *** MAIN FUNCTION ***
def main():
    # Init the pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
    # Load images
    background = pygame.image.load("field.png")
    img_orc = pygame.image.load("orc.png")
    # Create instance of class
    # From what I can dicern...
    # source image = img_orc
    # frames = 4
    # modes = 1???
    # width = 32
    # height = 48
    # FPS will remain 3.0
    orc = Char(img_orc, 4, 1, 32, 48)
    # Game loop
    while pygame.event.poll().type != KEYDOWN:
        screen.blit(background,(0,0))
        screen.blit(orc.image,orc.get_pos())
        orc.update(pygame.time.get_ticks(),SCREEN_W,SCREEN_H)
        pygame.display.update()
        pygame.time.delay(10)

if __name__ == '__main__': main()
