import pygame

class Bullet:
    def __init__(self,x,y,dx,dy,height,width):
        self.mX=x
        self.mY=y
        self.mDx=dx
        self.mDy=dy 
        self.mScreenHeight=height
        self.mScreenWidth=width
    
    def getX(self):
        return self.mX
    
    def getY(self):
        return self.mY
    
    def getDx(self):
        return self.mDx
    
    def getDy(self):
        return self.mDy
    
    def setX(self):
        if self.mX>self.mScreenWidth:
            self.mX=0
        else:
            self.mX+=self.mDx
        
    def setY(self):
        if self.mY>self.mScreenHeight:
            self.mY=0
        else:
            self.mY+=self.mDy
    
    def setDx(self,value):
        self.mDx=value
    
    def setDy(self,value):
        self.mDy=value
    
    def drawBullet(self,surface):
        color=(255,255,255)
        center=(self.mX,self.mY)
        radius = 2
        pygame.draw.circle(surface, color, center, radius)
        
    def draw(self,surface):
        self.drawBullet(surface)