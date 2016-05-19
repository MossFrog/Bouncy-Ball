from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform
import os


# Software created by Kaan Ozcelik #

class Starter(PygameHelper):


    def __init__(self):
        
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))
        
        sky = pygame.image.load("sky.jpg").convert()
        self.sky = pygame.transform.scale(sky,(800,600))
       
        ball = pygame.image.load(os.path.join("data","ball1.png")).convert_alpha()
        self.ball = pygame.transform.scale(ball,(50,50))
        
        plank = pygame.image.load("plank.png").convert()
        self.plank = pygame.transform.scale(plank,(50,50))
        
        self.x = 1
        self.y = 1
        
        self.m = 5
        self.n = 0
        
        self.plankc = [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750]
        
        

    def update(self):
        self.x = self.x + self.m
        self.y = self.y + self.n
        
        #Reflective Properties Of Lateral Walls
        if self.x > 755:
            self.m = -self.m
            
        #Energy Dissipation.
        if self.y > 505:
            self.n = -self.n*0.8
            self.m = self.m*0.9
            self.y = 505
        if abs(self.m) < 0.5:
            self.m = 0
            self.n = 0

        if self.x < -5:
            self.m = -self.m
        if self.y < -5:
            self.n = -self.n
            
            
        #Gravitational force
        if self.y < 505:
            self.n = self.n+1
            
        
        
        
        
    def keyUp(self, key):
        pass
        
    def mouseUp(self, button, pos):
        if button == 1 and pos[0]<50 and pos[1] < 50:
            self.n = self.n-20
            self.m = self.m -15
        if button == 1 and pos[0]>750 and pos[1] < 50:
            self.n = self.n-20
            self.m = self.m +15
        
    def mouseMotion(self, buttons, pos, rel):
        pass
        
        
    def draw(self):
        self.screen.blit(self.sky, (0,0))  
        self.screen.blit(self.ball, (self.x,self.y))
        
        pygame.draw.rect(self.screen,(153,255,53), (0,0,50,50))
        pygame.draw.rect(self.screen,(153,255,53), (750,0,50,50))
        
        for i in self.plankc:
            self.screen.blit(self.plank, (i,550))
        
        
        
s = Starter()
s.mainLoop(60)

