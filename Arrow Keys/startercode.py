from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform
import sys,pygame


class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))
        
        self.xcord = 400
        self.ycord = 300
        self.speed = 4
        
        self.blobx = 200
        self.bloby = 200
        
		
        
    def update(self):
        
        speed = self.speed
        
        
        #SCREEN BOUNDARIES
        if self.xcord > 810:
            self.xcord = -10
        if self.xcord < -10:
            self.xcord = 810
            
        if self.ycord > 610:
            self.ycord = -10
        if self.ycord < -10:
            self.ycord = 610
            
        #BLOB BEHAVIOUR
        if sqrt((self.blobx - self.xcord)**2+(self.bloby - self.ycord)**2) < 50:
            if (self.blobx - self.xcord) < 0:
                self.blobx = self.blobx - speed
            if (self.blobx - self.xcord) > 0:
                self.blobx = self.blobx + speed
            
            if (self.bloby - self.ycord) < 0:
                self.bloby = self.bloby - speed
            if (self.bloby - self.ycord) > 0:
                self.bloby = self.bloby + speed
            
            if self.blobx < 5:
                self.blobx = 5
                
            if self.blobx > 795:
                self.blobx = 795
                
            if self.bloby < 5:
                self.bloby = 5
                
            if self.bloby > 595:
                self.bloby = 595
            
        #HANDLING KEY EVENTS
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.xcord = self.xcord -speed
        
        if keys[K_RIGHT]:
            self.xcord = self.xcord +speed
            
        if keys[K_UP]:
            self.ycord = self.ycord -speed
        
        if keys[K_DOWN]:
            self.ycord = self.ycord +speed
            
            
        #DRAWING METHODS    
        self.screen.fill((255,255,255))
        pygame.draw.circle(self.screen,(200,100,200),(self.blobx,self.bloby),10)
        pygame.draw.circle(self.screen,(0,0,0),(self.xcord,self.ycord),20)
        
                
        
    def keyUp(self, key):
        pass
        
    def mouseUp(self, button, pos):
        pass
        
    def mouseMotion(self, buttons, pos, rel):
        pass
        
    def draw(self):
        pass
        
s = Starter()
s.mainLoop(60)
